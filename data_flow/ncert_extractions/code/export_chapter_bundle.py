#!/usr/bin/env python3
"""Builds one chapter's complete, self-describing export bundle.

    python3 scripts/export_chapter_bundle.py BIO12O-ch03 \\
        --pdf "inputs/ncert/older/Class_12th/Biology/Old_ncert_Bio_Chapter_3.pdf" \\
        --title "Biology Class 12 (Older NCERT) - Chapter 3: Human Reproduction"

Writes everything under `exports/chapters/<CHAPTER>/`:

    README.md                  what each file is, in plain words
    manifest.json              provenance: which agent run fed every page, plus checksums
    <CHAPTER>_READER.html      clean render of the extracted data, no page scans
    <CHAPTER>_REVIEW.html      side-by-side QA: original scan beside the extraction
    <CHAPTER>_FULL_EXTRACT.md  the same content as Markdown, for reuse elsewhere
    <CHAPTER>_layout.json      the measured printed layout (step A2L)
    figures/                   figure/table/equation crops
    html_pages/                full-page renders (used by the REVIEW file only)
    vendor/                    KaTeX, vendored locally so equations render offline

Why a bundle and a manifest rather than loose files:

`docs/SPEC.md` releases chapters through `export_tables.py` after a sign-off row in
`review/releases.csv`; these HTML/Markdown files are NOT that release and must not be mistaken
for it. But they are wanted as real, keepable artifacts, so each bundle records exactly which
agent run produced every page it was built from (`steps/A2/out/<item>.<run>.json` and the A2S/
A2N/A2B/A2L siblings). That is what makes a bundle auditable later: if a page is re-read and its
run label changes, the manifest of an old bundle still says which version of the data it showed.

The manifest also records what is NOT complete, because a bundle that silently looks finished is
worse than one that states its gaps.
"""

import argparse
import datetime
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

_SIBLING_STEPS = ("A2S", "A2N", "A2B", "A2L")
_RUN_PRIORITY = {"adjudicated": 0, "retry2": 1, "retry1": 2, "runB": 3, "runA": 4}


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _run(cmd):
    """Run a build command, surfacing its output. Returns its stdout for the manifest."""
    print("  $ " + " ".join(cmd[1:]))
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.stdout.strip():
        for line in res.stdout.strip().splitlines():
            print("    " + line)
    if res.returncode != 0:
        print(res.stderr.strip()[:2000], file=sys.stderr)
        raise SystemExit(f"build step failed: {' '.join(cmd[1:])}")
    return res.stdout.strip()


def _page_provenance(chapter):
    """{page_key: {step: run_label}} -- exactly which agent run of every step fed this bundle."""
    prov = {}
    for path in glob.glob(rc.pp("steps", "A2", "out", f"{chapter}-p*.*.json")):
        m = re.match(rf"{re.escape(chapter)}-p(\d+)\.(\w+)\.json$", os.path.basename(path))
        if not m:
            continue
        page, run = int(m.group(1)), m.group(2)
        key = f"page_{page:03d}"
        prev = prov.setdefault(key, {})
        if "A2" not in prev or _RUN_PRIORITY.get(run, 9) < _RUN_PRIORITY.get(prev["A2"], 9):
            prev["A2"] = run
    for key in prov:
        page_num = int(key.split("_")[1])
        item = f"{chapter}-p{page_num:03d}"
        for step in _SIBLING_STEPS:
            best, best_pri = None, 99
            for path in glob.glob(rc.pp("steps", step, "out", f"{item}.*.json")):
                run = path.rsplit(".", 2)[-2]
                pri = _RUN_PRIORITY.get(run, 9)
                if pri < best_pri:
                    best, best_pri = run, pri
            if best:
                prov[key][step] = best
    return dict(sorted(prov.items()))


def _outstanding(chapter):
    """What this chapter still has queued, per step -- recorded so a bundle never looks more
    finished than it is."""
    out = {}
    for step in ("A2", "A2S", "A2N", "A2B", "A2L"):
        try:
            res = subprocess.run(
                [sys.executable, rc.pp("scripts", "run_step.py"), step,
                 "--list", "--chapters", chapter],
                capture_output=True, text=True, timeout=240)
            n = len([l for l in res.stdout.splitlines() if "|" in l])
        except (subprocess.SubprocessError, OSError):
            n = None
        out[step] = n
    return out


_README = """# {chapter} — export bundle

{title}

Built {built_at} from this pipeline's extracted data.

## What each file is

| File | What it is | Use it for |
|---|---|---|
| `{chapter}_READER.html` | The chapter rendered from the **extracted data only** — no page scans. | Reading. This is the clean render: selectable text, searchable, responsive. |
| `{chapter}_REVIEW.html` | **Side by side**: the original scanned page on the left, this pipeline's extraction on the right, page by page. | Checking extraction quality against the source. |
| `{chapter}_FULL_EXTRACT.md` | The same content as Markdown. | Feeding other tools, diffing, pasting elsewhere. |
| `{chapter}_layout.json` | The **measured printed layout** (step A2L): column structure, which colour fills each panel, how big each kind of text is relative to body prose, how each is aligned. | Rebuilding the page's real arrangement; restyling without re-measuring. |
| `{chapter}.pdf` | The reader page printed to A4 — one file to send to someone. | Sharing, printing. |
| `manifest.json` | Provenance and gaps: which agent run produced every page, file checksums, and what is still outstanding. | Auditing what a given bundle actually showed. |
| `figures/` | Figure, table and equation crops cut from the source pages. | Diagrams the text cannot carry. |
| `html_pages/` | Full-page renders. Used by the REVIEW file only. | — |
| `vendor/` | KaTeX, vendored locally so equations render with no network. | — |
| `fonts/` | TeX Gyre Bonum (a free Bookman Old Style metric clone, the book's body face) and Adventor (its display sans). | — |

## Two things to know

**This bundle is not a release.** `docs/SPEC.md` releases chapters through `export_tables.py`
after a sign-off row in `review/releases.csv`. These files are keepable artifacts built from the
same extracted data, not that release — do not substitute one for the other.

**The crops carry the source watermark.** The NCERT PDFs are scans with
`© NCERT / not to be republished` baked into the page bitmap — not a layer that can be switched
off (verified: no optional-content groups, no text objects, one raster per page). So every image
cut from them carries that mark. The READER file embeds **no page scans** for this reason, and
its text, headings, bold terms, table rows and equation LaTeX are this pipeline's own output and
carry no watermark. The figure crops inside it still do, because a diagram cannot be carried as
text; only redrawing them would change that.

## Completeness at build time

{gaps}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--title", default=None)
    args = ap.parse_args()

    if not os.path.exists(args.pdf):
        print(f"source PDF not found: {args.pdf}", file=sys.stderr)
        return 1

    chapter = args.chapter
    title = args.title or chapter
    out_dir = rc.pp("exports", "chapters", chapter)
    os.makedirs(out_dir, exist_ok=True)
    py = sys.executable
    sc = lambda n: rc.pp("scripts", n)  # noqa: E731

    print(f"building bundle for {chapter}")
    build_log = {}
    build_log["layout_data"] = _run([py, sc("build_html_layout_data.py"), chapter])
    common = ["--pdf", args.pdf] + (["--title", title] if args.title else [])
    build_log["markdown"] = _run([py, sc("export_ncert_chapter_review.py"), chapter] + common)
    build_log["review_html"] = _run([py, sc("export_ncert_chapter_html.py"), chapter] + common)
    build_log["reader_html"] = _run([py, sc("export_ncert_chapter_html.py"), chapter]
                                    + common + ["--no-scans"])

    # Gather what the builders wrote into one self-contained directory.
    review_dir = rc.pp("exports", "review")
    moves = [
        (os.path.join(review_dir, "html", f"{chapter}_READER.html"), f"{chapter}_READER.html"),
        (os.path.join(review_dir, "html", f"{chapter}_REVIEW.html"), f"{chapter}_REVIEW.html"),
        (os.path.join(review_dir, f"{chapter}_FULL_EXTRACT.md"), f"{chapter}_FULL_EXTRACT.md"),
        (os.path.join(review_dir, "html_data", f"{chapter}_layout.json"),
         f"{chapter}_layout.json"),
    ]
    copied = []
    for src, dest_name in moves:
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(out_dir, dest_name))
            copied.append(dest_name)
    for src_dir, dest_name in ((os.path.join(review_dir, f"{chapter}_figures"), "figures"),
                              (os.path.join(review_dir, f"{chapter}_html_pages"), "html_pages"),
                              (os.path.join(review_dir, "html", "vendor"), "vendor"),
                              (os.path.join(review_dir, "html", "fonts"), "fonts")):
        if os.path.isdir(src_dir):
            dest = os.path.join(out_dir, dest_name)
            if os.path.isdir(dest):
                shutil.rmtree(dest)
            shutil.copytree(src_dir, dest)
            copied.append(dest_name + "/")

    # The READER references ../CHAPTER_figures and vendor/ relative to exports/review/html;
    # inside the bundle those sit alongside it, so the hrefs are rewritten to match.
    for name in (f"{chapter}_READER.html", f"{chapter}_REVIEW.html"):
        path = os.path.join(out_dir, name)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
        html = (html.replace(f"../{chapter}_figures/", "figures/")
                    .replace(f"../{chapter}_html_pages/", "html_pages/"))
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)

    # A shareable PDF, printed from the READER page by headless Chrome. Chrome is used rather
    # than a Python HTML-to-PDF library because the page already carries real @page rules and
    # web fonts: printing it in the same engine that renders it is what makes the PDF match what
    # the reader shows, instead of a second renderer's approximation of it.
    reader = os.path.join(out_dir, f"{chapter}_READER.html")
    pdf_out = os.path.join(out_dir, f"{chapter}.pdf")
    chrome = next((c for c in (
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        shutil.which("google-chrome"), shutil.which("chromium")) if c and os.path.exists(c)), None)
    if chrome and os.path.exists(reader):
        try:
            subprocess.run([chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                            "--virtual-time-budget=20000", f"--print-to-pdf={pdf_out}",
                            "file://" + os.path.abspath(reader)],
                           capture_output=True, timeout=300)
        except (subprocess.SubprocessError, OSError) as exc:
            print(f"  (PDF step skipped: {exc})")
    elif not chrome:
        print("  (PDF step skipped: no Chrome/Edge/Chromium found)")

    files = {}
    for root, _dirs, names in os.walk(out_dir):
        for fn in sorted(names):
            if fn == "manifest.json":
                continue
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, out_dir)
            files[rel] = {"bytes": os.path.getsize(full), "sha256": _sha256(full)}

    outstanding = _outstanding(chapter)
    built_at = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    manifest = {
        "chapter": chapter,
        "title": title,
        "built_at": built_at,
        "built_by": "scripts/export_chapter_bundle.py",
        "source_pdf": os.path.relpath(args.pdf, rc.pp()) if args.pdf.startswith(rc.pp())
                      else os.path.basename(args.pdf),
        "this_is_not_a_release": (
            "docs/SPEC.md releases chapters via export_tables.py after a sign-off row in "
            "review/releases.csv. This bundle is a keepable artifact built from the same "
            "extracted data, not that release."
        ),
        "watermark": (
            "Source PDFs are scans with '(c) NCERT / not to be republished' baked into the page "
            "bitmap (no optional-content groups, no text objects -- verified). Every crop cut "
            "from them carries it. The READER file embeds no page scans; its text, headings, "
            "bold terms, table rows and equation LaTeX carry no watermark."
        ),
        "steps_still_outstanding_for_this_chapter": outstanding,
        "page_provenance": _page_provenance(chapter),
        "build_output": build_log,
        "files": files,
    }
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    gap_lines = []
    for step, n in outstanding.items():
        if n is None:
            gap_lines.append(f"- `{step}`: could not be determined at build time")
        elif n == 0:
            gap_lines.append(f"- `{step}`: complete")
        else:
            gap_lines.append(f"- `{step}`: **{n} item(s) still queued**")
    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(_README.format(chapter=chapter, title=title, built_at=built_at,
                                gaps="\n".join(gap_lines)))

    print(f"\nbundle: {os.path.relpath(out_dir, rc.pp())}")
    print(f"  files: {len(files)}  ({sum(v['bytes'] for v in files.values()) / 1e6:.1f} MB)")
    for step, n in outstanding.items():
        if n:
            print(f"  NOTE: {step} still has {n} item(s) queued for this chapter")
    return 0


if __name__ == "__main__":
    sys.exit(main())
