"""Step check for QSUBJ -- the real validation lives in scripts/qmap_plugins.py.

The mapping steps validate against the CLOSED list each item carried, not against a list this module
keeps. Two copies of a taxonomy drift, and the check would then disagree with the agent about what
was allowed -- so the plugin, which wrote the item, is the only thing that validates it. This module
exists because config/steps.yaml declares a check path for every step; it adds the shape rules that
do not depend on the carried list.
"""

import json


def check(output, item=None, record=None, root=".", **_kwargs):
    if not isinstance(output, dict):
        return False, "output is not a JSON object"
    if "error" in output:
        return True, "agent reported an error: %s" % output["error"]
    if not str(output.get("why") or "").strip():
        return False, ("`why` is empty: a mapping with no stated reason cannot be reviewed, and "
                       "every step in this chain narrows the next one's choices")
    if len(str(output.get("why")).split()) < 4:
        return False, "`why` is not a sentence: name the fact the correct answer depends on"
    return True, "ok"


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("output")
    args = ap.parse_args(argv)
    ok, message = check(json.load(open(args.output, encoding="utf-8")))
    print(("PASS  " if ok else "FAIL  ") + message)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
