#!/usr/bin/env python3
"""Pins how B1 harvests the official key's booklet-code set.

Why this file exists. `official_key_codes` is the ONLY thing that lets B1 reach
`trust: memory_based`: a paper whose page does not print its own booklet code can still be
corroborated against the codes the authoritative NTA key states. That makes the field unusually
dangerous to get wrong, because it is *trusted*. A missing code merely blocks an upgrade; a
SPURIOUS code actively causes damage, since an agent that finds a page-printed code absent from a
code set it has every reason to believe reads it as the key contradicting the page.

Both failure directions have happened on real data, which is what each test below pins:

  * Missing (2026-10-13): the parser knew only `BOOK[LET] CODE`, so the 2020 key's own spelling
    `BOOK : E1` matched nothing and 2020 returned ZERO codes; and 2018 publishes one key file per
    code with the code only in the FILE NAME, so it returned zero too. Four B1 workers reported
    the field unusable and correctly refused to upgrade anything.
  * Spurious (same day): `SET\\s*:?` with IGNORECASE read "a gene or set of genes" on page 30 of
    the 2016 phase-2 key as the code "of", making that sitting's set exactly ['OF']. A worker then
    downgraded a legitimately page-printed "Code - AA" to `unsure` for contradicting it. It was
    caught only because that worker said ['OF'] looked "suspiciously short".

Run: .venv/bin/python3 -m pytest tests/test_b1_key_codes.py -q
"""
import os
import sys

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_TESTS_DIR)
_SCRIPTS_DIR = os.path.join(_PROJECT_ROOT, "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from step_plugins import B1Plugin  # noqa: E402

_RE = B1Plugin._B1_KEY_CODE_RE
_FILENAME_RE = B1Plugin._B1_KEY_FILENAME_CODE_RE


def _codes(text):
    """Every code the pattern finds in `text`, the way _official_key_codes collects them."""
    out = set()
    for m in _RE.finditer(text):
        hit = next((g for g in m.groups() if g), None)
        if hit:
            out.add(hit.upper())
    return out


# --- the three real spellings an official key uses -------------------------------------------

def test_reads_test_booklet_code():
    assert _codes("TEST BOOKLET CODE : A") == {"A"}
    assert _codes("Booklet Code: E1") == {"E1"}


def test_reads_set_with_colon():
    assert _codes("SET : M1") == {"M1"}


def test_reads_bare_book_colon():
    """The 2020 key's spelling: 'BOOK : E1', with the word CODE absent entirely."""
    assert _codes("EXAM DATE : 13.09.2020\nBOOK : E1\nNATIONAL TESTING AGENCY") == {"E1"}


# --- prose must never produce a code ----------------------------------------------------------

def test_set_of_genes_is_not_a_code():
    """The exact sentence that poisoned 2016 phase-2. Two independent guards kill it: `SET` now
    requires its colon, and the code group is matched case-sensitively."""
    prose = "normal homologous chromosome so that a gene or set of genes is"
    assert _codes(prose) == set()


def test_lowercase_never_becomes_a_code():
    assert _codes("booklet code: of") == set()
    assert _codes("the book : of the year") == set()


def test_set_without_colon_is_not_a_code():
    assert _codes("a set AB of values") == set()


# --- codes carried in the key's FILE NAME ------------------------------------------------------

def test_filename_codes_are_read():
    assert _FILENAME_RE.search("NEET_answers-key_2018-AA.pdf").group(1) == "AA"
    assert _FILENAME_RE.search("NEET_answers-key_2018-ZZ.pdf").group(1) == "ZZ"


def test_filename_descriptive_suffixes_are_not_codes():
    """The same directory holds these three shapes; none names a booklet."""
    for name in ("NEET_answers-key_2019-neet.pdf",
                 "NEET_answers-key_2016-phase-1.pdf",
                 "NEET_answers-key_2026-Re_neet.pdf",
                 "NEET_answers-key_2017.pdf"):
        assert _FILENAME_RE.search(name) is None, name


# --- behaviour against the real corpus ---------------------------------------------------------

def test_real_years_have_plausible_code_sets():
    """Floors, not exact counts, so adding key files cannot fail this. Each of these years was
    measured after the fixes; before them, 2018, 2020 and 2021 were all zero."""
    for year, floor in ((2018, 19), (2019, 28), (2020, 48), (2021, 24),
                        (2022, 32), (2023, 48), (2024, 48)):
        got = B1Plugin._official_key_codes(year, "MAIN")
        assert len(got) >= floor, f"{year}: expected >= {floor} codes, got {len(got)}: {got}"
        assert all(c.isupper() for c in got), f"{year}: non-upper-case code in {got}"


def test_complete_cross_product_cannot_corroborate():
    """The rule I got wrong. If the key lists every letter-digit combination, a code of that shape
    matches by construction and the match proves nothing, so `memory_based` must be unavailable."""
    full_2021 = [f"{a}{b}" for a in "MNOP" for b in "123456"]          # 24 of 24
    ok, why = B1Plugin._key_codes_discriminating(full_2021)
    assert ok is False
    assert "by construction" in why


def test_selective_set_can_corroborate():
    """A set is selective only if it has real GAPS over the letters and digits it actually uses.
    Note the subtlety this test originally got wrong: `EFGH x 123` looks like "12 of 24" against
    digits 1-6, but the key never mentions 4, 5 or 6, so over its own observed space it is 12 of 12
    -- complete, and non-discriminating. The space is the one the key itself demonstrates, which is
    the only space a code could be drawn from. So the gap has to be inside that space."""
    partial = [f"{a}{b}" for a in "EFGH" for b in "123456"]
    for gone in ("E4", "F5", "G6", "H1", "E2"):
        partial.remove(gone)                                            # 19 of 24
    ok, why = B1Plugin._key_codes_discriminating(partial)
    assert ok is True
    assert "can fail" in why


def test_doubled_letter_set_can_corroborate():
    """2018's shape: AA..ZZ with gaps, which is why code-QQ correctly failed."""
    ok, _ = B1Plugin._key_codes_discriminating(
        ["AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "KK", "LL"])
    assert ok is True


def test_empty_set_cannot_corroborate():
    ok, why = B1Plugin._key_codes_discriminating([])
    assert ok is False
    assert "no code set" in why


def test_real_years_discriminating_power():
    """Measured on the real keys. The four 100% years are exactly the ones that wrongly upgraded
    49 items before this was computed rather than assumed."""
    for year in (2018, 2019, 2022):
        ok, why = B1Plugin._key_codes_discriminating(B1Plugin._official_key_codes(year, "MAIN"))
        assert ok is True, f"{year} should be selective: {why}"
    for year in (2020, 2021, 2023, 2024):
        ok, why = B1Plugin._key_codes_discriminating(B1Plugin._official_key_codes(year, "MAIN"))
        assert ok is False, f"{year} is a complete cross-product and must not corroborate: {why}"


def test_input_ships_the_caveat_with_the_data():
    """The set must never travel without the flag; the set alone reads as corroboration."""
    fields = B1Plugin._key_code_fields({"year": 2021, "sitting": "MAIN"})
    assert set(fields) == {"official_key_codes", "official_key_codes_can_fail",
                           "official_key_codes_note"}
    assert fields["official_key_codes_can_fail"] is False
    assert fields["official_key_codes"], "2021 should still have a non-empty code set"


def test_no_spurious_code_for_2016_phase_2():
    """It is correct for this to be EMPTY. That key does not state its codes in any readable form,
    and an empty set honestly says 'cannot corroborate' -- which is what B1's `unsure` is for."""
    assert B1Plugin._official_key_codes(2016, "PH2") == []
