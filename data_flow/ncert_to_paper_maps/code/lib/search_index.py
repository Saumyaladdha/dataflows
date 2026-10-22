"""A simple keyword search/rank over (id, text) pairs, used later by D-stage repeat-finding and
B-stage keyword search (D9/B7/B8). Real but deliberately simple: term-overlap scoring, no
external search engine.
"""
import re
from collections import Counter

_TOKEN_RE = re.compile(r"[A-Za-z0-9']+")

_STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "of", "in", "on", "and", "or", "to", "for",
    "which", "with", "by", "as", "at", "be", "that", "this", "it", "from", "following",
}


def tokenize(text):
    """Lowercase `text` and split it into alphanumeric tokens for keyword matching."""
    return _TOKEN_RE.findall((text or "").lower())


def _content_tokens(text):
    return [t for t in tokenize(text) if t not in _STOPWORDS]


def rank(query, items, limit=None):
    """Rank (id, text) pairs in `items` by keyword overlap with `query`. Score is the number of
    query tokens matched in the item, weighted by how often each matched token occurs in the
    item, with a mild penalty for longer items so a short, tightly-matching item outranks a
    long one that merely contains the same words once. Stopwords are ignored on both sides.
    Returns [(id, score), ...] sorted best-first; items with zero overlap are dropped. Pass
    `limit` to keep only the top N results."""
    q_tokens = set(_content_tokens(query))
    if not q_tokens:
        return []

    results = []
    for item_id, text in items:
        tokens = _content_tokens(text)
        if not tokens:
            continue
        counts = Counter(tokens)
        matched = q_tokens & counts.keys()
        if not matched:
            continue
        overlap = sum(counts[t] for t in matched)
        score = len(matched) + overlap / (10.0 + len(tokens))
        results.append((item_id, score))

    results.sort(key=lambda pair: pair[1], reverse=True)
    if limit is not None:
        results = results[:limit]
    return results


if __name__ == "__main__":
    items = [
        ("Q1", "The work done to raise a mass to height R above the surface of the earth"),
        ("Q2", "A stretched wire is melted and stretched n times its original length"),
        ("Q3", "Post-synaptic receptors and their role in neurotransmission at the synapse"),
        ("Q4", "Completely unrelated question about acid-base titration curves"),
    ]
    results = rank("work done raise mass height earth surface", items)
    assert results, "expected at least one match"
    assert results[0][0] == "Q1", results

    none_match = rank("quantum chromodynamics gluon", items)
    assert none_match == []

    empty_query = rank("", items)
    assert empty_query == []

    limited = rank("stretched wire melted", items, limit=1)
    assert len(limited) == 1 and limited[0][0] == "Q2"

    print("search_index.py self-check OK:", results)
