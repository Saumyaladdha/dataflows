#!/usr/bin/env python3
"""Spec 13.0's `codebook_version`: the content hash of a `codebook/*.md` file.

    python3 scripts/codebook_version.py --all            # every codebook a step reads
    python3 scripts/codebook_version.py --step E4        # one step's codebook text + hash
    python3 scripts/codebook_version.py --check-wiring   # what is still not wired, honestly

SPEC 13.0, verbatim: "If a file exists, the runner passes its full text to the agent as the
`codebook` field, and records its file hash as `codebook_version` on every tag it produced. If a
file is missing, the agent receives only the allowed values ... and `codebook_version = "none"`."

WHERE THE HASH SHOULD BE COMPUTED -- the answer, having looked:

`scripts/step_plugins.py` ALREADY has this function, as `_d_codebook(name)` (added during the
D1-D11 build), and `D11Plugin` already uses it to stamp `d11_codebook_version` on every record it
writes. So the claim repeated in all six `codebook/E*.md` STATUS sections -- "codebook_version is
computed and recorded nowhere in the codebase" -- is STALE: it is computed, for D11, and nowhere
else. What is actually missing is (a) `codebook_file:` is `null` for E1-E6 and D11 in
`config/steps.yaml` even though the files now exist, and (b) no E plugin exists yet to read it.

This module is therefore deliberately NOT a second implementation competing with that one. It is
byte-for-byte the same formula (sha256 of the file's raw bytes, first 12 hex characters, the
literal string "none" when the file is absent) so the two can never disagree, and the proposal is
one line of delegation in `step_plugins.py`:

    def _d_codebook(name):
        import codebook_version
        return codebook_version.load(name)

That keeps one formula in the repo and lets `scripts/checks/E4.py` verify an agent's claimed
`codebook_version` against the real file without importing `step_plugins.py` (which is a 7,000-line
module that pulls in the whole runner -- a check script must stay cheap and side-effect free).

Why a check needs to recompute it at all: E4's agent output carries `codebook_version` itself
(spec 13/E4 "Agent output"). If `codebook/E4.md` exists but the output says `"none"`, the codebook
never reached the agent -- a wiring failure that would otherwise pass every schema and every
value check in total silence while mis-tagging the bank. scripts/checks/E4.py fails on it.
"""
import argparse
import hashlib
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402

#: The literal `codebook_version` spec 13.0 requires when the file does not exist.
NONE = "none"

#: Which `codebook/<file>` each step reads (spec 13.0's own list, in step order).
STEP_CODEBOOK_FILE = {
    "D4": "D4_link_type.md",
    "D11": "D11.md",
    "E1": "E1.md",
    "E2": "E2.md",
    "E3": "E3.md",
    "E4": "E4.md",
    "E5": "E5.md",
    "E6": "E6.md",
}


def hash_bytes(raw):
    """sha256 of the file's raw bytes, first 12 hex chars -- identical to
    step_plugins._d_codebook, deliberately (see the module docstring)."""
    return hashlib.sha256(raw).hexdigest()[:12]


def load(name):
    """(text, version) for `codebook/<name>`; (None, "none") when the file does not exist.

    `name` is the file name, e.g. "E4.md" -- the same argument step_plugins._d_codebook takes."""
    path = rc.pp("codebook", name)
    if not os.path.exists(path):
        return None, NONE
    with open(path, "rb") as f:
        raw = f.read()
    return raw.decode("utf-8"), hash_bytes(raw)


def for_step(step):
    """(text, version) for the codebook `step` reads; (None, "none") for a step with none."""
    name = STEP_CODEBOOK_FILE.get(step)
    if not name:
        return None, NONE
    return load(name)


def version_for_step(step):
    return for_step(step)[1]


def _check_wiring():
    """Report the real wiring state. Prints nothing it cannot verify from the files themselves."""
    rows = []
    cfg = rc.load_steps_config()
    for step, name in STEP_CODEBOOK_FILE.items():
        text, ver = load(name)
        declared = (cfg.get(step) or {}).get("codebook_file")
        rows.append((step, name, "present" if text else "ABSENT", ver, declared))

    width = max(len(r[1]) for r in rows)
    print(f"{'step':<5} {'codebook file':<{width}} {'on disk':<8} {'version':<14} "
          f"steps.yaml codebook_file")
    for step, name, on_disk, ver, declared in rows:
        print(f"{step:<5} {name:<{width}} {on_disk:<8} {ver:<14} {declared!r}")

    unwired = [r[0] for r in rows if r[2] == "present" and not r[4]]
    print()
    if unwired:
        print(f"NOT WIRED: {', '.join(unwired)} -- the codebook file exists on disk but "
              f"config/steps.yaml still says codebook_file: null, so no runner will load it "
              f"and every tag these steps produce will record codebook_version = \"none\".")
        print("The YAML needed to fix this is in config/_pending_E_entries.yaml "
              "(scripts/step_plugins.py and config/steps.yaml are owned by another agent).")
    else:
        print("every codebook that exists on disk is declared in config/steps.yaml")
    return 1 if unwired else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="spec 13.0 codebook_version (content hash).")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--all", action="store_true", help="Every codebook a step reads.")
    g.add_argument("--step", help="One step, e.g. E4.")
    g.add_argument("--check-wiring", action="store_true",
                   help="Which codebooks exist on disk but are not declared in steps.yaml.")
    ap.add_argument("--text", action="store_true", help="With --step, also print the full text.")
    args = ap.parse_args(argv)

    if args.check_wiring:
        return _check_wiring()

    if args.all:
        for step, name in STEP_CODEBOOK_FILE.items():
            text, ver = load(name)
            print(f"{step:<5} {name:<16} {ver:<14} "
                  f"{'(' + str(len(text)) + ' chars)' if text else '(file absent)'}")
        return 0

    text, ver = for_step(args.step)
    print(f"{args.step} codebook_version = {ver}")
    if args.text and text:
        print()
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
