#!/usr/bin/env python3
"""Proof that scripts/runner_core.py's NCERT path/filename parsing numbers every real chapter
PDF correctly, and in particular that the three Class-11 older-edition filename shapes added on
2026-10-12 are not silently mis-numbered.

Why this test exists. Class-11 older NCERT was reported missing when 60 real chapter PDFs
existed; fixing the intake walk exposed two ways the chapter number could go quietly wrong, both
confirmed against the real PDFs' own text rather than inferred:

  1. FRONT/BACK MATTER IS NOT A CHAPTER. "1 Prelims.pdf", "10 Appendices.pdf" and
     "11 Answers.pdf" all open with a bare number that looks exactly like the sort-order prefix
     on a real chapter file ("10 9. Biomolecules.pdf"). A parser that reads the leading digits
     would register them as chapters 1, 10 and 11 -- inventing three chapters and colliding with
     three real ones. They must return None.

  2. PART-VOLUME CHAPTER NUMBERS RESTART. Class-11 older Chemistry ships as two part volumes
     (P1/, P2/) and each volume's filenames number its chapters from 1. The real chapter numbers
     are P1 = 1-7 and P2 = 8-14, proven by the volumes' own back matter: P1's Answers.pdf indexes
     UNIT 1,2,5,6,7 and P2's indexes UNIT 8,12,13; P2's chapter bodies state "UNIT 9" (Hydrogen),
     "UNIT 11" (p-Block), "UNIT 13" (Hydrocarbons) and "UNIT 14" (Environmental Chemistry).
     Taking P2's filename numbers at face value would register chapters 1-7 twice for one book
     and lose seven real chapters.

The contiguity assertion below is the one that would have caught either defect: a book whose
chapters are not exactly 1..N, each once, is mis-numbered regardless of which shape caused it.

Run: .venv/bin/python3 -m pytest tests/test_ncert_file_parsing.py   (or via pytest tests/)
"""
import collections
import os
import sys

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_TESTS_DIR)
_SCRIPTS_DIR = os.path.join(_PROJECT_ROOT, "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402

# Files that carry no chapter number at all. Each is real front or back matter, verified by
# opening it: Prelims is the title/imprint/contents matter, Appendices is reference tables,
# Answers is the exercise answer index. Registering any of them as a chapter would be wrong.
NON_CHAPTER_FILES = [
    "older/Class_11th/Biology/1 Prelims.pdf",
    "older/Class_11th/Physics/1 Prelims.pdf",
    "older/Class_11th/Physics/10 Appendices.pdf",
    "older/Class_11th/Physics/11 Answers.pdf",
    "older/Class_11th/Chemistry/P1/1 Prelims.pdf",
    "older/Class_11th/Chemistry/P1/9 Appendices.pdf",
    "older/Class_11th/Chemistry/P1/10 Answers.pdf",
    "older/Class_11th/Chemistry/P2/1 Prelims.pdf",
    "older/Class_11th/Chemistry/P2/9 Answers.pdf",
]

# (relpath, expected chapter number). Spot checks on every filename shape in the real drop,
# including both Class-11 older shapes and all three pre-existing patterns, so a change aimed at
# the new shapes cannot regress the old ones.
EXPECTED = [
    # Class-11 older, "<sort order> <chapter>. <Title>.pdf" -- the second number is the chapter
    ("older/Class_11th/Biology/10 9. Biomolecules.pdf", 9),
    ("older/Class_11th/Biology/11 10. Cell Cycle and Cell Division.pdf", 10),
    ("older/Class_11th/Biology/2 1. The Living World.pdf", 1),
    ("older/Class_11th/Biology/23 22. Chemical Coordination and Integration.pdf", 22),
    ("older/Class_11th/Physics/9 8. Gravitation.pdf", 8),
    # Class-11 older Physics Part II, "<chapter>. <Title>.pdf" -- no sort-order prefix at all
    ("older/Class_11th/Physics/9. Mechanical Properties Of Solids.pdf", 9),
    ("older/Class_11th/Physics/11. Thermal Properties Of Matter.pdf", 11),
    ("older/Class_11th/Physics/15. Waves.pdf", 15),
    # Class-11 older Chemistry: P1 as written, P2 offset past P1's seven chapters
    ("older/Class_11th/Chemistry/P1/2 1. Some Basic Concepts of Chemistry.pdf", 1),
    ("older/Class_11th/Chemistry/P1/8 7. Equilibrium.pdf", 7),
    ("older/Class_11th/Chemistry/P2/2 1. Redox Reactions.pdf", 8),
    ("older/Class_11th/Chemistry/P2/3 2. Hydrogen.pdf", 9),
    ("older/Class_11th/Chemistry/P2/5 4. The p-Block Elements.pdf", 11),
    ("older/Class_11th/Chemistry/P2/7 6. Hydrocarbons.pdf", 13),
    ("older/Class_11th/Chemistry/P2/8 7. Environmental Chemistry.pdf", 14),
    # Pre-existing patterns (docs/OPEN_QUESTIONS.md 2026-10-09) must keep working
    ("latest/Class_12th/Chemistry/Chapter_1.pdf", 1),
    ("latest/Class_11th/Biology/Chapter_19.pdf", 19),
    ("older/Class_12th/Chemistry/CH-16.pdf", 16),
    ("older/Class_12th/Biology/Old_ncert_Bio_Chapter_7.pdf", 7),
    ("older/Class_12th/Physics/Old_ncert_Physics_Chapter_15.pdf", 15),
]

# The lab manual is a book, not a chapter set, and must not acquire a chapter number from its
# filename ("...-ssmclk_menual.pdf" contains no chapter number; nothing should be invented).
LAB_MANUAL = "lab_manuals/senior-secondary-microscale-chemistry-laboratory-kit-ssmclk_menual.pdf"


def test_non_chapter_files_have_no_chapter_number():
    for relpath in NON_CHAPTER_FILES:
        got = rc.parse_ncert_relpath(relpath)["chapter_num"]
        assert got is None, (
            f"{relpath} is front/back matter, not a chapter, but was numbered {got} -- "
            f"this invents a chapter and collides with a real one"
        )


def test_expected_chapter_numbers():
    for relpath, expected in EXPECTED:
        got = rc.parse_ncert_relpath(relpath)["chapter_num"]
        assert got == expected, f"{relpath}: expected chapter {expected}, got {got}"


def test_lab_manual_has_no_chapter_number():
    assert rc.parse_ncert_relpath(LAB_MANUAL)["chapter_num"] is None


def test_every_real_book_has_contiguous_unique_chapters():
    """The invariant that catches a mis-numbering however it arises: for each
    (edition, class, subject) group of real files on disk, the chapter numbers must be exactly
    1..N with no duplicate and no gap."""
    books = collections.defaultdict(list)
    for relpath, _abspath in rc.iter_ncert_files():
        parsed = rc.parse_ncert_relpath(relpath)
        if parsed["edition_code"] == "lab_manual" or parsed["chapter_num"] is None:
            continue
        key = (parsed["edition_folder"], parsed["class_num"], parsed["subject"])
        books[key].append((parsed["chapter_num"], relpath))

    assert len(books) == 12, (
        f"expected 12 NCERT chapter sets (3 subjects x 2 classes x 2 editions), found "
        f"{len(books)}: {sorted(books)}"
    )

    for key, entries in sorted(books.items(), key=lambda kv: str(kv[0])):
        nums = [n for n, _ in entries]
        counts = collections.Counter(nums)
        dupes = {n: [r for c, r in entries if c == n] for n, c in counts.items() if c > 1}
        assert not dupes, f"{key}: duplicate chapter numbers {dupes}"
        assert sorted(nums) == list(range(1, len(nums) + 1)), (
            f"{key}: chapter numbers are not 1..{len(nums)} -- got {sorted(nums)}"
        )


if __name__ == "__main__":
    test_non_chapter_files_have_no_chapter_number()
    test_expected_chapter_numbers()
    test_lab_manual_has_no_chapter_number()
    test_every_real_book_has_contiguous_unique_chapters()
    print("tests/test_ncert_file_parsing.py: all checks passed")
