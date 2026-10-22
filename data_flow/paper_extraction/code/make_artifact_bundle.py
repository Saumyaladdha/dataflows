"""Build a publishable bundle: the page, plus every image it uses, under one root.

WHY THIS IS A SCRIPT AND NOT A ONE-OFF
--------------------------------------
A published artifact is served from its own root, so it cannot carry a path that climbs out of that
root -- and the built page references its images exactly that way (`../papers_v2/crops/...`,
`../steps/A2/work/...`), because on disk they live in the pipeline's own directories. Every publish
therefore needs the same three steps: copy each image in under a flat name, rewrite the page to
point at the copies, and emit the published-path map. Doing that by hand cost a broken publish once
already -- a hand-pasted file map was truncated and 17 of 42 files never shipped, so every NCERT
page scan was a broken image for anyone who opened it.

It also strips the `file://` links to the source PDFs. They resolve only on the machine that built
the page, and they print its folder structure to whoever opens it.
"""

import argparse
import json
import os
import re
import shutil


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", help="the built HTML page")
    ap.add_argument("out_dir", help="bundle directory to write")
    ap.add_argument("--files-json", help="also write the published-path map here")
    args = ap.parse_args()

    base = os.path.dirname(os.path.abspath(args.source))
    assets = os.path.join(args.out_dir, "assets")
    # A stale asset from a previous build would still be published, and would still count against
    # the 255-file limit, so the directory is rebuilt rather than added to.
    if os.path.isdir(assets):
        shutil.rmtree(assets)
    os.makedirs(assets)

    with open(args.source, encoding="utf-8") as fh:
        html = fh.read()

    mapping, used, missing = {}, set(), []
    for src in sorted(set(re.findall(r'src="([^"]+)"', html))):
        if src.startswith("data:"):
            continue
        path = os.path.normpath(os.path.join(base, src))
        if not os.path.exists(path):
            missing.append(src)
            continue
        # The flat name keeps the origin readable, so a booklet crop is still tellable from an
        # NCERT page scan when someone inspects the published bundle.
        flat = re.sub(r"[^A-Za-z0-9._-]", "_", os.path.relpath(path, os.path.dirname(base)))
        flat = flat.lstrip("_")
        assert flat not in used, "two images would publish to the same name: %s" % flat
        used.add(flat)
        shutil.copy2(path, os.path.join(assets, flat))
        mapping[src] = "assets/" + flat

    for src, dest in mapping.items():
        html = html.replace('src="%s"' % src, 'src="%s"' % dest)
    html = re.sub(r'<a href="file://[^"]*">[^<]*</a>', "", html)
    html = html.replace(" &middot; </div>", "</div>")

    with open(os.path.join(args.out_dir, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(html)

    files = {("assets/" + f): ("assets/" + f) for f in sorted(os.listdir(assets))}
    if args.files_json:
        with open(args.files_json, "w", encoding="utf-8") as fh:
            json.dump(files, fh, indent=0)

    total = sum(os.path.getsize(os.path.join(assets, f)) for f in os.listdir(assets))
    print("bundle      %s" % args.out_dir)
    print("images      %d   %.1f MB total   largest %.1f MB"
          % (len(files), total / 1048576,
             max(os.path.getsize(os.path.join(assets, f)) for f in os.listdir(assets)) / 1048576))
    print("index.html  %.0f KB" % (len(html) / 1024))
    print("publish     %d file(s) + index.html" % len(files))
    if missing:
        print("MISSING, left as links: %s" % ", ".join(missing[:5]))
    assert len(files) <= 255, "a published artifact takes at most 255 supporting files"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
