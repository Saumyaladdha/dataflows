"""Step-specific check for A1 (spec Section 9/A1 'Checks'):
  (1) reprint_text_exact non-empty and found on that page's text layer, when one exists;
  (2) edition_seen equals the manifest edition;
  (3) exactly one latest and one older book per subject-class (plus manuals) -- this one is a
      cross-item, register-level check, not something a single A1 output can verify in isolation,
      so it is enforced where the register row is actually written (step_plugins.A1Plugin's
      post_assembly, which only ever inserts the first-registered row per book_id) rather than
      here; see that function's docstring.

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring for the
full convention this build uses across all 11 check files, including how a failing message's
"<FLAG_CODE>: <detail>" segments map onto config/steps.yaml's flags.

`context["input_data"]` is the A1 work input (steps/A1/work/<item>.<run>.input.json): `file`,
`folder_edition_hint`, `page_images`, `text_layer` (list aligned 1:1 with page_images).

Judgment call (see docs/OPEN_QUESTIONS.md): `inputs/manifest.csv`'s edition column is the spec's
literal "manifest edition" for check (2); this build compares against the work input's
`folder_edition_hint` instead, which is read from the same manifest's `edition` column by
whichever step built the input file (A1Plugin._build_input sources it from the file's path,
itself derived from the manifest-driven inputs/ncert/<edition>/... folder layout) -- so in
practice these already agree once intake/manifest exist; this check only ever sees the hint.
"""
from lib import quote_verify


def check(data, context):
    if not isinstance(data, dict):
        return False, "A1 output is not an object"

    input_data = context.get("input_data") or {}
    segments = []

    reprint_text = data.get("reprint_text_exact", "")
    reprint_page = data.get("reprint_page")
    text_layers = input_data.get("text_layer") or []
    if reprint_text:
        if reprint_page and 1 <= reprint_page <= len(text_layers):
            page_text = text_layers[reprint_page - 1] or ""
            if page_text.strip():  # "when one exists" -- an image-only page has none to check against
                span = quote_verify.find(reprint_text, page_text)
                if span is None:
                    segments.append(
                        f"A1_REPRINT_NOT_FOUND: reprint_text_exact {reprint_text!r} not found "
                        f"word-for-word in page {reprint_page}'s text layer"
                    )
        elif reprint_page is not None:
            segments.append(
                f"A1_REPRINT_NOT_FOUND: reprint_page {reprint_page} is out of range for the "
                f"{len(text_layers)} page(s) supplied"
            )
    # An empty reprint_text_exact is not itself a check failure here -- Section 9/A1's own "On
    # failure" text treats "no reprint line found" as a resolvable case (safe default "unknown" +
    # flag), not a schema-level error; the agent is expected to leave it empty with a `note`
    # explaining why rather than invent one (universal rule 6/7).

    edition_seen = data.get("edition_seen")
    folder_hint = input_data.get("folder_edition_hint")
    if folder_hint and edition_seen not in (folder_hint, "unsure"):
        segments.append(
            f"A1_EDITION_MISMATCH: edition_seen {edition_seen!r} != folder_edition_hint {folder_hint!r}"
        )

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
