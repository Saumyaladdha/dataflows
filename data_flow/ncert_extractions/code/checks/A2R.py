#!/usr/bin/env python3
"""Check for A2R (a2r-render-reviewer): one rendered page judged against the book page.

Shape only -- it cannot second-guess a visual judgement. What it enforces is that the verdict and
the findings agree with each other, because the failure mode that matters here is a review that
says "matches" while listing defects, or lists a defect with no description anyone can act on.
"""
import json
import sys


def check(path):
    try:
        with open(path, encoding="utf-8") as fh:
            rec = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        return False, "unreadable: %s" % exc

    verdict = rec.get("verdict")
    if verdict not in ("matches", "minor_differences", "content_missing", "unusable"):
        return False, "verdict must be matches, minor_differences, content_missing or unusable"
    if not (rec.get("note") or "").strip():
        return False, "note is required"

    findings = rec.get("findings")
    if not isinstance(findings, list):
        return False, "findings must be a list"
    if verdict == "matches" and findings:
        return False, "verdict=matches but findings were listed"
    if verdict != "matches" and not findings:
        return False, "verdict=%s but no findings given" % verdict

    kinds = ("missing", "duplicated", "clipped", "misplaced", "formatting", "blank_space")
    for i, f in enumerate(findings):
        if f.get("kind") not in kinds:
            return False, "findings[%d].kind is not one of %s" % (i, ", ".join(kinds))
        what = (f.get("what") or "").strip()
        if len(what) < 25:
            return False, ("findings[%d].what is too vague to act on -- name the figure, "
                           "equation or heading and say what differs" % i)

    # A page that lost content must say so in its verdict, whatever order the findings are in.
    if any(f.get("kind") == "missing" for f in findings) and verdict in ("matches",
                                                                        "minor_differences"):
        return False, ("a `missing` finding means content the book prints is absent; the verdict "
                       "must be content_missing or unusable")
    return True, "ok"


if __name__ == "__main__":
    ok, msg = check(sys.argv[1])
    print(msg)
    sys.exit(0 if ok else 1)
