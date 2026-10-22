#!/usr/bin/env python3
"""Upload a chapter's figure/table crops and a book's furniture to the CDN, and record the URLs.

    export ARIVIHAN_TOKEN=...            # from the verify-otp call
    export ARIVIHAN_USER_ID=...
    python code/upload_assets.py --chapter BIO11L-ch01 --dry-run
    python code/upload_assets.py --chapter BIO11L-ch01
    python code/upload_assets.py --furniture BIO11

THE CREDENTIAL IS NEVER IN THIS FILE, AND NEVER IN THE REPO.
It is read from `ARIVIHAN_TOKEN` / `ARIVIHAN_USER_ID` at run time. The token is a short-lived
bearer for a real staging account: committed once, it is in the history for good, and anyone
with the repo can upload as that user. Re-issue it with the send-otp / verify-otp pair rather
than pasting it anywhere.

WHAT GETS UPLOADED, AND WHAT ONLY ONCE
----------------------------------------
  per chapter   every figure and table crop             figures/p007_fig01.png
  per BOOK      the header art, the folio art, fonts    assets/furniture/BIO11/

The furniture is uploaded ONCE per book and reused by every page of every chapter. Uploading it
per chapter would put 71 copies of the same header on the CDN and -- worse -- let them drift:
measured before the shared-asset change, one chapter held 25 crops of a single header, 8 of them
broken 295-byte near-empties. One URL per book means one appearance for every page.

WHAT IS WRITTEN BACK
----------------------
On each figure/table node of `chapter.json`:

    "image":        "https://cdn…/…/p007_fig01.png"    what a renderer loads
    "image_local":  "figures/p007_fig01.png"           the fallback, still on disk
    "image_sha256": "…"                                so a re-upload is skipped

`image_sha256` is what makes the script safe to re-run: a crop whose bytes have not changed is
not uploaded again, so running it after every extraction costs nothing for the parts that did
not move.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

UPLOAD_URL = ("https://platform-stage.arivihan.com/internal-metrics/secure/upload/api/v1/files"
              "?uploadType=general&folderPath={folder}&targetDpi={dpi}")


def _slug(v):
    """`Reprint 2026-27` -> `2026-27`; anything else made safe for a URL path segment."""
    t = re.sub(r"^\s*Reprint\s+", "", str(v or "")).strip()
    t = re.sub(r"[^A-Za-z0-9._-]+", "-", t).strip("-")
    return t


def _creds():
    token = os.environ.get("ARIVIHAN_TOKEN")
    user = os.environ.get("ARIVIHAN_USER_ID")
    if not token or not user:
        raise SystemExit(
            "ARIVIHAN_TOKEN and ARIVIHAN_USER_ID must be set.\n"
            "  curl .../auth/send-otp   -d '{\"phoneNumber\":\"…\"}'\n"
            "  curl .../auth/verify-otp -d '{\"phoneNumber\":\"…\",\"otp\":\"…\"}'\n"
            "then: export ARIVIHAN_TOKEN=…  ARIVIHAN_USER_ID=…")
    return token, user


def _multipart(path):
    boundary = uuid.uuid4().hex
    name = os.path.basename(path)
    with open(path, "rb") as fh:
        data = fh.read()
    body = b"".join([
        f"--{boundary}\r\n".encode(),
        f'Content-Disposition: form-data; name="files"; filename="{name}"\r\n'.encode(),
        b"Content-Type: image/png\r\n\r\n", data, b"\r\n",
        f"--{boundary}--\r\n".encode(),
    ])
    return body, f"multipart/form-data; boundary={boundary}"


def upload(path, folder, dpi=300, timeout=60):
    """POST one file, return the CDN URL the API reports."""
    token, user = _creds()
    body, ctype = _multipart(path)
    req = urllib.request.Request(
        UPLOAD_URL.format(folder=folder, dpi=dpi), data=body, method="POST",
        headers={"accept": "*/*", "userId": user, "token": token, "Content-Type": ctype})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        payload = json.loads(r.read().decode("utf-8", "replace"))
    return _find_url(payload) or payload


def _find_url(obj):
    """The API's response shape is not pinned here -- find the first http(s) string in it.

    Deliberate: hard-coding `payload["data"][0]["url"]` makes this break silently the day the
    envelope changes, and the thing we need is unambiguous in the body either way.
    """
    if isinstance(obj, str):
        return obj if obj.startswith("http") else None
    if isinstance(obj, dict):
        for k in ("url", "fileUrl", "cdnUrl", "location", "path"):
            v = obj.get(k)
            if isinstance(v, str) and v.startswith("http"):
                return v
        for v in obj.values():
            u = _find_url(v)
            if u:
                return u
    if isinstance(obj, list):
        for v in obj:
            u = _find_url(v)
            if u:
                return u
    return None


def _sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _nodes(tree):
    for n in tree:
        yield n
        if n.get("children"):
            yield from _nodes(n["children"])


def chapter_assets(chapter_dir, dry_run=False, dpi=300):
    """Upload every crop this chapter's tree points at, and record the URLs in chapter.json."""
    jpath = os.path.join(chapter_dir, "chapter.json")
    with open(jpath, encoding="utf-8") as fh:
        doc = json.load(fh)
    # A CDN PATH SEGMENT MUST BE URL-SAFE.
    #
    # The imprint is whatever the book prints, and Class 12 Biology prints "Reprint 2026-27"
    # where Class 11 prints "2024-25". The space made the request URL invalid and every
    # upload for that chapter died before it was sent -- a whole chapter silently unuploadable
    # because of one character in a book's imprint line.
    folder = (f"ncert/{_slug(doc.get('reprint')) or 'unknown'}/{doc['book_id']}/"
              f"ch{doc['chapter']['number']:02d}")
    done = skipped = failed = 0
    for node in _nodes(doc["tree"]):
        local = node.get("image_local")
        if not local:
            continue
        path = os.path.join(chapter_dir, local)
        if not os.path.exists(path):
            continue
        sha = _sha(path)
        if node.get("image") and node.get("image_sha256") == sha:
            skipped += 1
            continue
        if dry_run:
            print(f"   would upload {local}  -> {folder}")
            done += 1
            continue
        try:
            url = upload(path, folder, dpi=dpi)
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError) as e:
            print(f"   FAILED {local}: {e}", file=sys.stderr)
            failed += 1
            continue
        if not isinstance(url, str):
            print(f"   FAILED {local}: no url in response {str(url)[:160]}", file=sys.stderr)
            failed += 1
            continue
        node["image"] = url
        node["image_sha256"] = sha
        done += 1

    # THE PAGE'S OWN ARTWORK IS AN ASSET TOO.
    #
    # Only tree nodes were uploaded, so a chapter's figures went to the CDN while the header
    # band, the chapter banner and the QR code -- which live on the PAGE record rather than
    # the tree, because they are furniture and not content -- stayed as local paths. That
    # gives a page that loads its diagrams from the CDN and its banner from a folder the
    # recipient does not have. Every image a renderer resolves must come from one place.
    for page in doc.get("pages") or []:
        for art in (page.get("art") or []):
            local = art.get("file")
            if not local:
                continue
            path = os.path.join(chapter_dir, local)
            if not os.path.exists(path):
                continue
            sha = _sha(path)
            if art.get("url") and art.get("sha256") == sha:
                skipped += 1
                continue
            if dry_run:
                print(f"   would upload {local}  -> {folder}")
                done += 1
                continue
            try:
                u = upload(path, folder, dpi=dpi)
                if isinstance(u, str):
                    art["url"] = u
                    art["sha256"] = sha
                    done += 1
                else:
                    failed += 1
            except Exception as exc:                          # noqa: BLE001
                print(f"   FAILED {local}: {exc}")
                failed += 1

    if not dry_run:
        with open(jpath, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, indent=1, ensure_ascii=False)
    return done, skipped, failed


def furniture_assets(design_key, dry_run=False, dpi=300):
    """Upload a BOOK's shared furniture once, and record the URLs beside it."""
    d = os.path.join(ROOT, "assets", "furniture", design_key)
    if not os.path.isdir(d):
        raise SystemExit(f"no furniture for {design_key}; run build_furniture_assets.py first")
    out_path = os.path.join(d, "cdn.json")
    urls = {}
    if os.path.exists(out_path):
        with open(out_path, encoding="utf-8") as fh:
            urls = json.load(fh)
    folder = f"ncert/furniture/{design_key}"
    for name in sorted(os.listdir(d)):
        if not name.lower().endswith((".png", ".otf", ".woff2")):
            continue
        path = os.path.join(d, name)
        sha = _sha(path)
        if urls.get(name, {}).get("sha256") == sha:
            continue
        if dry_run:
            print(f"   would upload {design_key}/{name} -> {folder}")
            continue
        url = upload(path, folder, dpi=dpi)
        urls[name] = {"url": url, "sha256": sha}
    if not dry_run:
        with open(out_path, "w", encoding="utf-8") as fh:
            json.dump(urls, fh, indent=1, ensure_ascii=False)
    return urls


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", help="e.g. BIO11L-ch01")
    ap.add_argument("--chapter-dir", help="path to a chapter folder")
    ap.add_argument("--furniture", help="a design key, e.g. BIO11")
    ap.add_argument("--all", action="store_true", help="every chapter under data/")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--dpi", type=int, default=300)
    a = ap.parse_args()

    if a.furniture:
        urls = furniture_assets(a.furniture, a.dry_run, a.dpi)
        print(f"{a.furniture}: {len(urls)} furniture assets")
        return

    import glob
    dirs = []
    if a.chapter_dir:
        dirs = [a.chapter_dir]
    elif a.all:
        dirs = sorted(os.path.dirname(p) for p in
                      glob.glob(os.path.join(ROOT, "data", "*", "class_*", "*", "*",
                                             "chapter.json")))
    elif a.chapter:
        for p in glob.glob(os.path.join(ROOT, "data", "*", "class_*", "*", "*",
                                        "chapter.json")):
            with open(p, encoding="utf-8") as fh:
                doc = json.load(fh)
            if f"{doc['book_id']}-ch{doc['chapter']['number']:02d}" == a.chapter:
                dirs = [os.path.dirname(p)]
                break
    if not dirs:
        raise SystemExit("nothing to do: pass --chapter, --chapter-dir, --all or --furniture")
    for d in dirs:
        done, skipped, failed = chapter_assets(d, a.dry_run, a.dpi)
        print(f"{os.path.relpath(d, ROOT)}: {done} uploaded, {skipped} unchanged, "
              f"{failed} failed")


if __name__ == "__main__":
    main()
