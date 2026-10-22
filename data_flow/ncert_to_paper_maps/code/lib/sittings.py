"""The official NEET sitting calendar for 2016-2026, verbatim from spec Section 8 / S0's
procedure step 3: "for each year 2016-2026, for each sitting on the official list ... Known
sittings that must exist: 2016 MAIN and PH2; 2019 MAIN and REEXAM; 2020 MAIN and REEXAM; 2024
MAIN and RETEST; 2026 CANCELLED (3 May) and REEXAM (21 June); MAIN for every other year."

Shared by scripts/build_manifest.py (so it knows which years can't safely assume a lone paper
file is the MAIN sitting) and scripts/intake_check.py (so it knows exactly what S0 must require).
Keeping this list in one place means the two scripts can never quietly disagree about the
calendar.
"""

REQUIRED_SITTINGS = {
    2016: ["MAIN", "PH2"],
    2017: ["MAIN"],
    2018: ["MAIN"],
    2019: ["MAIN", "REEXAM"],
    2020: ["MAIN", "REEXAM"],
    2021: ["MAIN"],
    2022: ["MAIN"],
    2023: ["MAIN"],
    2024: ["MAIN", "RETEST"],
    2025: ["MAIN"],
    2026: ["CANCELLED", "REEXAM"],
}

# Spec Section 8/S0 procedure step 4 and Section 2.7: 2016-2026 is in scope; everything else
# (2013-2015 pending Section 20 decision #1, and anything before that) is out of scope for now.
IN_SCOPE_YEARS = set(REQUIRED_SITTINGS)

# Years where the official calendar has more than one sitting, i.e. a bare filename with no
# sitting marker in it genuinely cannot be trusted to mean MAIN.
MULTI_SITTING_YEARS = {year for year, s in REQUIRED_SITTINGS.items() if len(s) > 1}

# A cancelled sitting is, by definition, never scored and so never gets an official final key
# (confirmed in NEET_PYQ_Input_Collection_Codebook.md Section 3: "expected: a cancelled sitting
# has no final key"). Judgment call (see docs/OPEN_QUESTIONS.md, 2026-10-09, Section 8/S0): S0
# requires a *paper* for every sitting on the calendar including CANCELLED, but does not require
# a *key* for a CANCELLED sitting.
SITTINGS_WITHOUT_KEY_REQUIREMENT = {"CANCELLED"}
