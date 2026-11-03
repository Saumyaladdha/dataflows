#!/usr/bin/env python3
"""Find the NCERT sentence a rated question rests on, from the chapter it was already filed under.

    python3 code/find_ncert_lines.py --paper 2017_A --subject biology
    python3 code/find_ncert_lines.py --paper 2017_A --subject biology --apply

WHY THIS EXISTS
---------------
`asks: fact_line` says "this question wants a fact NCERT states". Until now nothing checked that
claim: the rater decided it from the SHAPE of the question -- a stem asking what/who/where and
options that are bare names -- and never opened an NCERT file. That is a claim about a book,
made without reading the book, and on 2017_A q092 it happened to be right, which is worse than
being wrong because it reads as evidence.

So this reads the book. Every question already carries the chapter and subtopics an earlier step
filed it under, so the search starts THERE -- the filed chapter, scored sentence by sentence --
and only widens to all 32 biology chapters when the filed chapter has nothing that matches. A
line found in the filed chapter and a line found by a desperate whole-book sweep are not equally
good evidence, so the two cases are reported apart and `scope` records which happened.

WHAT A MATCH IS
---------------
Overlap of CONTENT words between the question (stem + the keyed option + the rating's concept)
and one printed sentence, weighted so a rare word like `halophiles` counts for much more than
`which` or `found`. That is a retrieval score, not a judgement: the script says "this sentence
is the closest thing the chapter prints", and a human still has to agree it is the line. Nothing
here edits a rating's label -- it attaches evidence beside it.
"""

import argparse
import collections
import glob
import json
import math
import os
import re

NCERT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                     "ncert_extractions", "data", "new_ncert")
STOP = set("""a an the of to in and or is are was were be been being for from with without on at
by as that this these those it its which what who where when how why not no all any each such
some more most other than then there here into onto upon over under about above below during
can may might must should would could do does did done have has had having i ii iii iv v
following given above shown figure fig table also both either neither only same different
between among within against through across after before because since so if but while both""".split())


def _sentences(path):
    """[(sentence, page, kind)] for one chapter.json, in printed order."""
    doc = json.load(open(path, encoding="utf-8"))

    def walk(ns):
        for n in ns:
            yield n
            for c in n.get("children") or []:
                yield from walk([c])

    out = []
    for n in walk(doc.get("tree") or []):
        body = (n.get("body") or "").strip()
        if not body:
            continue
        page = (n.get("pages") or [None])[0]
        # The extraction already filed each block under a subtopic of its chapter. That is the
        # narrowest place to look, and it is why the cascade can have a middle tier at all.
        sub = n.get("agent_subtopic_name") or ""
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", body):
            s = " ".join(s.split())
            if len(s) > 24:
                out.append((s, page, n.get("kind"), sub))
    return out


def _words(text):
    return [w for w in re.findall(r"[a-z]{3,}", (text or "").lower()) if w not in STOP]


def _index(sents):
    """Document frequency over the sentences, so common words stop carrying the match."""
    df = collections.Counter()
    for rec in sents:
        df.update(set(_words(rec[0])))
    return df


def score(query_words, sent, df, n_docs):
    sw = set(_words(sent))
    if not sw:
        return 0.0
    hit = sw & set(query_words)
    if not hit:
        return 0.0
    # idf, so `halophiles` outweighs `found`
    val = sum(math.log(1 + n_docs / (1 + df.get(w, 0))) for w in hit)
    return val / math.sqrt(len(sw))


def chapters(subject):
    out = {}
    for p in sorted(glob.glob(os.path.join(NCERT, "class_*", subject, "*", "chapter.json"))):
        out[os.path.basename(os.path.dirname(p))] = p
    return out


def pick_chapter(name, available):
    """The NCERT directory whose name best matches the chapter the question was filed under."""
    if not name:
        return None
    want = set(_words(name))
    best, score_ = None, 0.0
    for key in available:
        got = set(_words(key.split("_", 1)[-1].replace("-", " ")))
        if not got:
            continue
        v = len(want & got) / len(want | got)
        if v > score_:
            best, score_ = key, v
    return best if score_ >= 0.34 else None


def find(paper_id, subject, apply_=False, top=2):
    year = paper_id.split("_")[0]
    export = json.load(open(os.path.join("data", year, paper_id, "questions.json"),
                            encoding="utf-8"))
    by_id = {r["question_id"]: r for r in export["questions"]}

    avail = chapters(subject)
    if not avail:
        raise SystemExit("no NCERT %s chapters under %s" % (subject, NCERT))
    cache, idx_cache = {}, {}

    def sents_for(key):
        if key not in cache:
            cache[key] = _sentences(avail[key])
            idx_cache[key] = _index(cache[key])
        return cache[key], idx_cache[key]

    rated, results = [], []
    for p in sorted(glob.glob("steps/ECAT/out/ex__%s__%s__*.json" % (paper_id, subject))):
        doc = json.load(open(p, encoding="utf-8"))
        for r in doc["ratings"]:
            rated.append((p, doc, r))

    for path, doc, r in rated:
        row = by_id.get(r["question_id"]) or {}
        q = row.get("question") or {}
        cls = row.get("classification") or {}
        filed = (cls.get("chapter") or {}).get("name")
        subs = [s.get("name") for s in (cls.get("subtopics") or []) if isinstance(s, dict)]
        key_opt = ""
        for o in q.get("options") or []:
            if str(o.get("key")) == str((row.get("answer") or {}).get("publisher")):
                key_opt = o.get("text") or ""
        query = _words(" ".join([q.get("stem") or "", key_opt, r.get("concept") or "",
                                 " ".join(subs)]))

        target = pick_chapter(filed, avail)

        def sweep(keys, only_subtopics=None):
            """Score every sentence in `keys`; if subtopics are given, only those blocks."""
            got = []
            want = {w for sname in (only_subtopics or []) for w in _words(sname)}
            for key in keys:
                sents, df = sents_for(key)
                n = len(sents)
                for sent, page, kind, sub in sents:
                    if want:
                        sw = set(_words(sub))
                        # the block's own subtopic has to overlap the question's
                        if not sw or len(sw & want) < max(1, min(2, len(want) // 3)):
                            continue
                    v = score(query, sent, df, n)
                    if v > 0:
                        got.append((v, key, page, kind, sent, sub))
            got.sort(reverse=True, key=lambda h: h[0])
            return got

        # THE CASCADE: narrowest first, widening only when the narrow look comes up short.
        #
        # 1. THE SUBTOPIC the question was filed under, inside the chapter it was filed under.
        #    The extraction labelled every block with its subtopic, so this is a handful of
        #    paragraphs -- the pages a teacher would actually open.
        # 2. THE WHOLE CHAPTER, when the subtopic label was missing or too narrow.
        # 3. EVERY CHAPTER, last. A line found here is still a real line, but the question was
        #    filed somewhere it does not live -- which is itself worth knowing, and is how the
        #    four 2017 questions sitting on deleted syllabus showed up.
        #
        # The tier is recorded, because a hit in tier 1 and a hit in tier 3 are not equally
        # good evidence and a reviewer must be able to tell them apart.
        hits, tier = [], "none"
        if target and subs:
            hits = sweep([target], subs)
            tier = "subtopic"
        if not hits or hits[0][0] < 3.2:
            if target:
                wider = sweep([target])
                if wider and (not hits or wider[0][0] > hits[0][0]):
                    hits, tier = wider, "chapter"
        if not hits or hits[0][0] < 3.2:
            allhits = sweep(sorted(avail))
            if allhits and (not hits or allhits[0][0] > hits[0][0]):
                hits, tier = allhits, "all_chapters"
        if not target:
            tier += " (filed chapter '%s' is not in this NCERT edition)" % (filed or "?")

        results.append({
            "question_id": r["question_id"], "qno": row.get("qno"),
            "asks": r.get("asks"), "filed_chapter": filed, "ncert_chapter": target,
            "subtopics": subs, "scope": tier,
            "lines": [{"quote": sent, "chapter": key, "page": page, "kind": kind,
                       "ncert_subtopic": sub, "score": round(v, 2)}
                      for v, key, page, kind, sent, sub in hits[:top]],
            "_path": path, "_doc": doc, "_rating": r,
        })
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", required=True)
    ap.add_argument("--subject", default="biology")
    ap.add_argument("--apply", action="store_true",
                    help="attach the top line to each rating as `ncert`")
    ap.add_argument("--min-score", type=float, default=3.2,
                    help="below this the match is reported but NOT attached")
    a = ap.parse_args()

    res = find(a.paper, a.subject)
    strong = 0
    for r in res:
        top = r["lines"][0] if r["lines"] else None
        mark = " "
        if top and top["score"] >= a.min_score:
            strong += 1
            mark = "*"
        print("\n%s q%-4s %-16s filed=%s" % (mark, r["qno"], r["asks"], r["filed_chapter"]))
        print("   scope: %s" % r["scope"])
        for ln in r["lines"]:
            print("   %5.2f  %s p%s" % (ln["score"], ln["chapter"], ln["page"]))
            print("          \"%s\"" % ln["quote"][:230])
    print("\n%d of %d have a line scoring >= %.1f" % (strong, len(res), a.min_score))

    if not a.apply:
        print("(nothing written -- pass --apply)")
        return 0

    touched = {}
    for r in res:
        top = r["lines"][0] if r["lines"] else None
        if not top or top["score"] < a.min_score:
            continue
        r["_rating"]["ncert"] = {
            "quote": top["quote"], "chapter": top["chapter"], "page": top["page"],
            "found_by": "find_ncert_lines.py, %s" % r["scope"],
        }
        touched[r["_path"]] = r["_doc"]
    for path, doc in touched.items():
        json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("attached an NCERT line to %d rating(s) across %d file(s)" % (strong, len(touched)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
