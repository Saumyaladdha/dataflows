#!/usr/bin/env python3
"""Publish a chapter with CDN links ONLY: no local `figures/...` path left in its files.

    export ARIVIHAN_TOKEN=...  ARIVIHAN_USER_ID=...
    python code/cdn_publish.py BIO11L-ch02
    python code/cdn_publish.py BIO11L-ch02 --dry-run

Run it LAST, after `run_chapter.py` (or after any rebuild). It

  1. uploads every image the chapter points at that has no CDN URL yet -- figure and table
     crops on the tree, and the page art (header band, QR code, page ground);
  2. rewrites chapter.json so each image field IS its CDN URL: a page art's `file` becomes the
     URL, and a node's `image_local` (the local fallback) is removed, `image` being the link;
  3. re-renders chapter.md, chapter-exact.html and the DynamoDB rows from that
     JSON, so all of them carry the same links.

WHY A SIDE MAP, `figures/_cdn_map.json`
-----------------------------------------
`upload_assets.py` and the rebuild's carry-forward both find a crop by its local path. Once
chapter.json holds only URLs, neither can, so a rebuild would come back with local paths and
no links, and re-uploading would put a second copy of every unchanged crop on the CDN. The map
records `file name -> {url, sha256}` beside the crops (it is local bookkeeping, never shipped):
after a rebuild this script restores the link of every crop whose BYTES are unchanged and
uploads only what actually changed. Running it twice uploads nothing.

A file whose upload fails keeps its local path and the run reports it, rather than writing a
link that does not exist.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import upload_assets          # noqa: E402

MAP_NAME = "_cdn_map.json"


def _sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def chapter_dir(cid):
    """The chapter's output folder, from the id (`BIO11L-ch02`)."""
    import book_design as design_lib
    import build_chapter_json as bcj
    m = re.fullmatch(r"([A-Z]{3}\d{2}[LO])-ch(\d+)", cid)
    if not m:
        raise SystemExit(f"bad chapter id {cid!r}; expected like BIO11L-ch02")
    book_id, num = m.group(1), int(m.group(2))
    subject, klass, edition = design_lib.parse_book_id(book_id)
    base = os.path.join(ROOT, "data", "new_ncert" if edition == "L" else "old_ncert",
                        f"class_{klass}", bcj.SUBJECT_WORD[subject])
    hits = [d for d in os.listdir(base) if d.startswith(f"ch{num:02d}_")] if os.path.isdir(base) else []
    if len(hits) != 1:
        raise SystemExit(f"{cid}: expected one ch{num:02d}_* folder under {base}, found {hits}")
    return os.path.join(base, hits[0])


def _walk(nodes):
    for n in nodes or []:
        yield n
        yield from _walk(n.get("children"))


def publish(cid, dry_run=False):
    cdir = chapter_dir(cid)
    jpath = os.path.join(cdir, "chapter.json")
    mpath = os.path.join(cdir, "figures", MAP_NAME)
    with open(jpath, encoding="utf-8") as fh:
        doc = json.load(fh)
    cmap = {}
    if os.path.exists(mpath):
        with open(mpath, encoding="utf-8") as fh:
            cmap = json.load(fh)
    folder = (f"ncert/{upload_assets._slug(doc.get('reprint')) or 'unknown'}/{doc['book_id']}/"
              f"ch{doc['chapter']['number']:02d}")
    stats = {"uploaded": 0, "reused": 0, "already": 0, "failed": []}

    def link(local, known_url=None, known_sha=None):
        """CDN URL for the crop at `local` (relative to the chapter), or None."""
        if not local or local.startswith("http"):
            return local
        path = os.path.join(cdir, local)
        if not os.path.exists(path):
            stats["failed"].append(f"{local} (missing on disk)")
            return None
        sha = _sha(path)
        name = os.path.basename(local)
        if known_url and known_sha == sha:
            stats["already"] += 1
            cmap[name] = {"url": known_url, "sha256": sha}
            return known_url
        hit = cmap.get(name)
        if hit and hit.get("sha256") == sha:
            stats["reused"] += 1
            return hit["url"]
        if dry_run:
            print(f"   would upload {local} -> {folder}")
            stats["uploaded"] += 1
            return None
        # A CHANGED CROP NEEDS A NEW URL. The upload API names the file `<stem>_<ddmmyyyy>.png`,
        # so re-uploading changed bytes under the same name on the same day reuses the old URL,
        # and CloudFront keeps serving the cached old picture (query strings are ignored):
        # BIO11L ch03's Table 3.1 crop grew from a header strip to the whole table and would
        # have kept showing the strip. A crop the map already knows with other bytes goes up as
        # `<stem>-<sha8>.png`, whose URL has never been served.
        up = path
        if hit:
            import shutil
            import tempfile
            stem, ext = os.path.splitext(name)
            up = os.path.join(tempfile.mkdtemp(prefix="cdn_"), f"{stem}-{sha[:8]}{ext}")
            shutil.copyfile(path, up)
        try:
            url = upload_assets.upload(up, folder)
        except Exception as exc:                                  # noqa: BLE001
            stats["failed"].append(f"{local} ({exc})")
            return None
        if not isinstance(url, str):
            stats["failed"].append(f"{local} (no url in response)")
            return None
        cmap[name] = {"url": url, "sha256": sha}
        stats["uploaded"] += 1
        return url

    for n in _walk(doc.get("tree")):
        # Each lettered panel is its own picture and gets its own link (`cut_figures`).
        for q in n.get("panels") or []:
            if not q.get("image_local"):
                continue
            url = link(q["image_local"], q.get("image"), q.get("image_sha256"))
            if url and not dry_run:
                q["image"] = url
                q["image_sha256"] = cmap.get(os.path.basename(q["image_local"]), {}).get(
                    "sha256", q.get("image_sha256"))
                del q["image_local"]
        # A figure we drew ourselves (step FIGP) is its own file with its own link.
        if n.get("image_drawn") and not n["image_drawn"].startswith("http"):
            local = n["image_drawn"]
            url = link(local, None, None)
            if url and not dry_run:
                n["image_drawn"] = url
                n["image_drawn_sha256"] = cmap.get(os.path.basename(local), {}).get("sha256")
        if not n.get("image_local"):
            continue
        url = link(n["image_local"], n.get("image"), n.get("image_sha256"))
        if url and not dry_run:
            n["image"] = url
            n["image_sha256"] = cmap.get(os.path.basename(n["image_local"]), {}).get(
                "sha256", n.get("image_sha256"))
            del n["image_local"]
    for page in doc.get("pages") or []:
        for art in page.get("art") or []:
            url = link(art.get("file"), art.get("url"), art.get("sha256"))
            if url and not dry_run:
                art["sha256"] = cmap.get(os.path.basename(art["file"]), {}).get(
                    "sha256", art.get("sha256"))
                art["url"] = url
                art["file"] = url

    if dry_run:
        return cdir, stats
    with open(jpath, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False)
    with open(mpath, "w", encoding="utf-8") as fh:
        json.dump(cmap, fh, indent=1, sort_keys=True)

    # Every file is derived from chapter.json, so they are rendered from the JSON just written
    # -- never rebuilt, which would re-extract the tree and bring the local paths back.
    # chapter.html is not a deliverable (2026-10-24): chapter-exact.html, chapter.json and
    # chapter.md are, so only those are written.
    import build_chapter_json as bcj
    import render_exact
    with open(os.path.join(cdir, "chapter.md"), "w", encoding="utf-8") as fh:
        fh.write(bcj.to_markdown(doc))
    render_exact.write(doc, cdir)
    r = subprocess.run([sys.executable, os.path.join(HERE, "export_rows.py"), cid],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode:
        stats["failed"].append(f"export_rows: {(r.stderr or '').strip()[:200]}")
    return cdir, stats


def local_refs(cdir):
    """Every `figures/...` path still written in a deliverable file -- should be none."""
    out = {}
    for name in ("chapter.json", "chapter.md", "chapter-exact.html"):
        if not os.path.exists(os.path.join(cdir, name)):
            continue
        with open(os.path.join(cdir, name), encoding="utf-8") as fh:
            out[name] = sorted(set(re.findall(r"figures/[\w.-]+\.(?:png|jpe?g|svg)", fh.read())))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter_id")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cdir, st = publish(a.chapter_id, dry_run=a.dry_run)
    print(f"{os.path.relpath(cdir, ROOT)}: {st['uploaded']} uploaded, {st['reused']} reused "
          f"from map, {st['already']} already linked, {len(st['failed'])} failed")
    for f in st["failed"]:
        print("   FAILED", f)
    if not a.dry_run:
        left = {k: v for k, v in local_refs(cdir).items() if v}
        print("   local paths left:", left or "none")
        if left or st["failed"]:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
