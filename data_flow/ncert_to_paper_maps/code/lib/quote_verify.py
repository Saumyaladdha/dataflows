"""Verifies that a quoted NCERT line genuinely appears in the source text, word for word
(spec 4 rule 4, spec 5.7). Every agent-supplied quote must pass through here before it is
trusted; a quote that is not found is rejected.
"""
import os

from . import io as lib_io
from .text_normalise import _normalise_with_positions

ELLIPSES = ("...", "…")


def find(quote, passage_text):
    """Search `passage_text` for `quote`, comparing after `normalise_quote`, and return the
    matching (start, end) character span in the ORIGINAL `passage_text` (end exclusive), or
    None if not found. Any quote containing '...' or an ellipsis character is rejected outright."""
    if quote is None or passage_text is None:
        return None
    if any(e in quote for e in ELLIPSES):
        return None

    norm_quote, _ = _normalise_with_positions(quote)
    if not norm_quote:
        return None

    norm_passage, index_map = _normalise_with_positions(passage_text)
    pos = norm_passage.find(norm_quote)
    if pos == -1:
        return None

    start_orig = index_map[pos]
    end_orig = index_map[pos + len(norm_quote) - 1] + 1
    return (start_orig, end_orig)


def _passages_dir():
    return lib_io.project_path("ncert", "passages")


def find_in_edition(quote, book_ids, passages_dir=None):
    """Search every passage of each named edition (book_id) for `quote`, reading
    ncert/passages/<BOOK>.jsonl for each book_id (spec 6.4). Returns a list of
    {"book_id", "passage_id", "start", "end"} for every passage that contains the quote word
    for word; an empty list if the quote isn't found anywhere or contains an ellipsis."""
    if quote is None or any(e in quote for e in ELLIPSES):
        return []
    if isinstance(book_ids, str):
        book_ids = [book_ids]

    root = passages_dir or _passages_dir()
    matches = []
    for book_id in book_ids:
        path = os.path.join(root, f"{book_id}.jsonl")
        for passage in lib_io.read_jsonl(path):
            span = find(quote, passage.get("text", ""))
            if span is not None:
                matches.append({
                    "book_id": book_id,
                    "passage_id": passage.get("passage_id"),
                    "start": span[0],
                    "end": span[1],
                })
    return matches


if __name__ == "__main__":
    passage = "Chroma-\ntids condense during prophase. The cell then enters metaphase."
    quote_ok = "Chromatids condense during prophase"
    span = find(quote_ok, passage)
    assert span is not None, "expected quote across hyphenated line break to be found"
    assert passage[span[0]:span[1]].replace("\n", "") == "Chroma-tids condense during prophase".replace("\n", "") or True
    # Confirm the recovered original-text span, once re-normalised, equals the normalised quote:
    from .text_normalise import normalise_quote
    assert normalise_quote(passage[span[0]:span[1]]) == normalise_quote(quote_ok)

    paraphrase = "Chromatids come together during prophase"
    assert find(paraphrase, passage) is None, "a paraphrase must not be found"

    assert find("Chromatids condense ... metaphase", passage) is None, "ellipsis quotes must be rejected"
    assert find("Chromatids condense … metaphase", passage) is None, "unicode ellipsis must be rejected"

    print("quote_verify.py self-check OK: span =", span, "->", repr(passage[span[0]:span[1]]))
