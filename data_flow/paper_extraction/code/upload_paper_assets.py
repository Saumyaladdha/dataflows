#!/usr/bin/env python3
"""Upload every image of the v2 paper corpus to the CDN, and record each URL on its question.

    export ARIVIHAN_TOKEN=...  ARIVIHAN_USER_ID=...      # code/cdn_login.py prints these
    python3 code/upload_paper_assets.py --dry-run
    python3 code/upload_paper_assets.py                        # every booklet
    python3 code/upload_paper_assets.py --paper-id 2024_Q2
    python3 code/upload_paper_assets.py --check                # fail if any image has no CDN link

THE RULE THIS STEP ENFORCES: every image this pipeline cuts is saved as a CDN link. See lib/cdn.py
for where the URL lives on a record and why it is keyed by path.

WHAT GETS UPLOADED
------------------
Every picture a question record points at, whichever step cut it:

    crops/<paper>/q###.png                       the question as printed       extract_paper_v2.py
    solutions/<paper>/q###.png                   the printed worked solution   extract_paper_v2.py
    figures/<paper>/q###_<role>_N.png            a figure found by geometry    extract_paper_v2.py
    figures_agent/<paper>/q###.png               the figure the agent boxed    cut_agent_figures.py
    figures_agent/<paper>/q###_option_K.png      one picture option            cut_agent_figures.py

into `neet_papers/<year>/<paper>/<kind>/` on the CDN, so a question crop and an agent figure that
share a file name (`q017.png`) never land in the same folder.

WHEN IT RUNS
------------
After every step that cuts images: once after `extract` (question crops, solution crops, geometric figures) and
again after `cut_agent_figures.py` (agent figures, option crops). `run_paper_pipeline.py` does both.
It is safe to repeat: a file whose bytes match the `sha256` recorded with its URL is not uploaded
again, so only what a step actually re-cut goes up.

A link to a picture the record no longer names is DROPPED, not kept. cut_agent_figures.py rewrites
`agent_figure_images` on every run, and a stale URL beside a fresh path is a page showing the
previous run's picture with nothing to say it is stale.
"""

import argparse
import collections
import glob
import json
import os
import sys
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
from lib import cdn  # noqa: E402

CORPUS = rc.corpus()


def paper_paths(paper_id=None):
    paths = sorted(glob.glob(rc.pp(*CORPUS, "papers", "*.json")))
    if paper_id:
        paths = [p for p in paths if os.path.basename(p) == "%s.json" % paper_id]
    return paths


def folder_for(meta, paper_id, rel):
    """`neet_papers/<year>/<paper>/<kind>` -- the kind is the image's own top-level directory."""
    kind = rel.replace("\\", "/").split("/", 1)[0]
    return "/".join(cdn.slug(part) for part in
                    ("neet_papers", meta.get("year") or "unknown", paper_id, kind))


def upload_paper(path, dry_run, dpi, counts):
    with open(path, encoding="utf-8") as fh:
        paper = json.load(fh)
    meta = paper["meta"]
    paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
    changed = False
    for question in paper["questions"]:
        wanted = cdn.image_paths(question)
        links = question.get("cdn") or {}
        for stale in [p for p in links if p not in wanted]:
            del links[stale]
            counts["stale_dropped"] += 1
            changed = True
        for rel in wanted:
            local = rc.pp(*CORPUS, rel)
            if not os.path.exists(local):
                # Named by the record and absent on disk: there is nothing to upload, and pretending
                # otherwise would hide a crop the cutter failed to write.
                counts["missing_on_disk"] += 1
                print("   MISSING  %s (q%03d names it, no file)" % (rel, question["qno"]),
                      file=sys.stderr)
                continue
            digest = cdn.sha256(local)
            entry = links.get(rel) or {}
            if entry.get("url") and entry.get("sha256") == digest:
                counts["unchanged"] += 1
                continue
            folder = folder_for(meta, paper_id, rel)
            if dry_run:
                print("   would upload %s -> %s" % (rel, folder))
                counts["would_upload"] += 1
                continue
            try:
                url = cdn.upload(local, folder, dpi, name=cdn.versioned_name(local, digest))
            except urllib.error.HTTPError as exc:
                if exc.code in (401, 403):
                    # AN EXPIRED TOKEN FAILS EVERY FILE THE SAME WAY. The first run against a stale
                    # token tried all 363 crops of 2017_A and logged 363 identical 401s. Stop at the
                    # first one, keep what already uploaded, and say how to get a new token.
                    if changed and not dry_run:
                        question["cdn"] = links
                        cdn.write_url_fields(question)
                        with open(path, "w", encoding="utf-8") as fh:
                            json.dump(paper, fh, ensure_ascii=False, indent=1)
                    raise SystemExit("the CDN refused the token (HTTP %d) -- it has expired. Get a "
                                     "new one:\n  python code/cdn_login.py --phone <number>\n"
                                     "  python code/cdn_login.py --phone <number> --otp <otp>\n"
                                     "then export the two lines it prints and re-run this command; "
                                     "files already uploaded are skipped." % exc.code)
                print("   FAILED   %s: %s" % (rel, exc), file=sys.stderr)
                counts["failed"] += 1
                continue
            except (urllib.error.URLError, ValueError, OSError) as exc:
                print("   FAILED   %s: %s" % (rel, exc), file=sys.stderr)
                counts["failed"] += 1
                continue
            links[rel] = {"url": url, "sha256": digest}
            counts["uploaded"] += 1
            changed = True
        question["cdn"] = links
        cdn.write_url_fields(question)
    if changed and not dry_run:
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(paper, fh, ensure_ascii=False, indent=1)
    return paper_id


def stale_links(paper_id=None, workers=16):
    """([(paper_path, qno, rel)], total) for every link whose SERVED bytes are not the recorded
    ones -- what a reader's browser would get, not what was sent."""
    import concurrent.futures
    jobs = []
    for path in paper_paths(paper_id):
        with open(path, encoding="utf-8") as fh:
            paper = json.load(fh)
        for question in paper["questions"]:
            for rel, entry in (question.get("cdn") or {}).items():
                if entry.get("url") and entry.get("sha256"):
                    jobs.append((path, question["qno"], rel, entry["url"], entry["sha256"]))

    def served(job):
        """Stale when the copy a browser gets (Brotli) is older than the copy now stored (plain)."""
        try:
            browser = cdn.served_version(job[3], "gzip, deflate, br")
            stored = cdn.served_version(job[3], "identity")
            return job, browser[0] != stored[0]
        except (urllib.error.URLError, OSError, ValueError):
            return job, True

    out = []
    with concurrent.futures.ThreadPoolExecutor(workers) as pool:
        for job, is_stale in pool.map(served, jobs):
            if is_stale:
                out.append((job[0], job[1], job[2]))
    return out, len(jobs)


def without_link(paper_id=None):
    """[(paper_id, qno, rel)] for every image that has no CDN URL recorded."""
    out = []
    for path in paper_paths(paper_id):
        with open(path, encoding="utf-8") as fh:
            paper = json.load(fh)
        meta = paper["meta"]
        pid = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
        for question in paper["questions"]:
            for rel in cdn.image_paths(question):
                if not cdn.url_for(question, rel):
                    out.append((pid, question["qno"], rel))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper-id", help="one booklet; omit for every booklet in the corpus")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="upload nothing; exit 1 if any image lacks a CDN link")
    ap.add_argument("--verify", action="store_true",
                    help="fetch every link as a browser does; with --apply, re-upload each one whose "
                         "served bytes are not the recorded ones (a stale CDN cache)")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dpi", type=int, default=0,
                    help="targetDpi sent to the CDN (default: the booklet's own crop dpi)")
    args = ap.parse_args()

    paths = paper_paths(args.paper_id)
    if not paths:
        print("no v2 papers found -- run code/extract_paper_v2.py --apply first")
        # Under --dry-run the extract step did not run either, so an empty corpus is expected.
        return 0 if args.dry_run else 1

    if args.check:
        missing = without_link(args.paper_id)
        for pid, qno, rel in missing[:20]:
            print("   no CDN link  %s q%03d  %s" % (pid, qno, rel))
        print("%d image(s) without a CDN link" % len(missing))
        return 1 if missing else 0

    if args.verify:
        stale, total = stale_links(args.paper_id)
        for _path, qno, rel in stale[:30]:
            print("   STALE  q%03d  %s" % (qno, rel))
        print("%d of %d link(s) serve browsers an older copy than the one stored" % (len(stale), total))
        if not stale or not args.apply:
            return 1 if stale else 0
        # forget those links, so the upload below sends each again under its fingerprinted name
        for path in sorted({s[0] for s in stale}):
            with open(path, encoding="utf-8") as fh:
                paper = json.load(fh)
            mine = {(qno, rel) for p, qno, rel in stale if p == path}
            for question in paper["questions"]:
                for qno, rel in mine:
                    if qno == question["qno"]:
                        (question.get("cdn") or {}).pop(rel, None)
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(paper, fh, ensure_ascii=False, indent=1)

    if not args.dry_run:
        cdn.creds()                   # fail before the first booklet, not halfway through it
    counts = collections.Counter()
    for path in paths:
        with open(path, encoding="utf-8") as fh:
            dpi = args.dpi or json.load(fh)["meta"].get("dpi") or 200
        before = dict(counts)
        paper_id = upload_paper(path, args.dry_run, dpi, counts)
        done = {k: counts[k] - before.get(k, 0) for k in counts if counts[k] - before.get(k, 0)}
        print("%-10s %s" % (paper_id, ", ".join("%s %d" % kv for kv in sorted(done.items()))
                            or "nothing to do"))
    print("\n%s" % ", ".join("%s %d" % kv for kv in sorted(counts.items())))
    if args.dry_run:
        print("(dry run -- nothing uploaded, nothing written)")
        return 0
    # Every image must end up as a CDN link; a failure or a missing file is not a pass.
    return 1 if (counts["failed"] or counts["missing_on_disk"]) else 0


if __name__ == "__main__":
    sys.exit(main())
