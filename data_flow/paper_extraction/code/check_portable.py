"""Prove the repo runs on a machine that has never seen the owner's folders.

WHY THIS EXISTS
---------------
The pipeline used to read its source booklets from `~/Downloads/Saumya_NEET_work/NEW/NEET_Papers`,
and the question records stored paths relative to that folder. Everything worked, on exactly one
machine. Handed to anyone else, the extractor would have failed on its first file and every "open
the source PDF" link on every exported page would have been dead -- while also printing the owner's
folder structure to whoever opened it.

This check fails if any of that comes back. It is cheap, so run it before any hand-off.

WHAT IT ALLOWS
--------------
A reference to the original tree inside a COMMENT, or as a documented fallback after the in-repo
path has been tried, is fine -- that is history and a convenience, not a dependency. What is not
allowed is a live path that only resolves on one machine.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import runner_core as rc                                      # noqa: E402

#: v1-era tools that still name the original tree. They are not on the live path -- nothing in
#: `config/steps.yaml` or any plugin calls them, and none of them touches `papers_v2` -- so they are
#: listed here rather than rewritten. If one is ever brought back into the flow, it has to be fixed
#: first, and this list is where that gets noticed.
LEGACY = {"build_manifest.py", "cross_code_match.py", "sitting_index.py", "verify_sources.py"}

OUTSIDE = re.compile(r"(~/Downloads|/Users/[a-z]+/Downloads|Saumya_NEET_work)")


def main():
    problems, allowed = [], []
    for name in sorted(os.listdir(rc.code_path())):
        if not name.endswith(".py") or name == os.path.basename(__file__):
            continue                      # this file names the paths it hunts for
        with open(rc.code_path(name), encoding="utf-8") as fh:
            for number, line in enumerate(fh, 1):
                if not OUTSIDE.search(line):
                    continue
                stripped = line.strip()
                is_comment = stripped.startswith("#") or stripped.startswith('"') \
                    or stripped.startswith("'") or stripped.startswith("*")
                if name in LEGACY:
                    allowed.append((name, number, "legacy tool, not on the live path"))
                elif is_comment or "EXTERNAL_ROOT" in line or "fallback" in line.lower():
                    allowed.append((name, number, "comment or documented fallback"))
                else:
                    problems.append((name, number, stripped[:88]))

    # Every source the corpus names must be inside the repo.
    import glob
    import json
    missing = []
    for path in sorted(glob.glob(rc.pp(*rc.corpus(), "papers", "*.json"))):
        with open(path, encoding="utf-8") as fh:
            rel = json.load(fh)["meta"]["source_pdf"]
        if not os.path.exists(rc.source_dir(rel)):
            missing.append(rel)

    print("portability check")
    print("  source booklets inside the repo: %d of %d"
          % (len(glob.glob(rc.pp(*rc.corpus(), "papers", "*.json"))) - len(missing),
             len(glob.glob(rc.pp(*rc.corpus(), "papers", "*.json")))))
    for rel in missing:
        print("    MISSING  %s" % rel)
    print("  references to the original tree, allowed: %d" % len(allowed))
    for name, number, why in allowed:
        print("    %-24s line %-5d %s" % (name, number, why))
    if problems:
        print("  LIVE PATHS THAT RESOLVE ON ONE MACHINE ONLY: %d" % len(problems))
        for name, number, text in problems:
            print("    %-24s line %-5d %s" % (name, number, text))
    print()
    print("FAIL" if (problems or missing) else "PASS")
    return 1 if (problems or missing) else 0


if __name__ == "__main__":
    raise SystemExit(main())
