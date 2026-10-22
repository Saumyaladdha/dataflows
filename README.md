# DATAFLOWS — NCERT extraction and NEET PYQ mapping

Turns NCERT textbook PDFs into a structured, citable representation: a semantic chapter tree
for search and question-mapping, and a page-faithful render that reproduces the printed book.

## What is here

```
data_flow/
  ncert_extractions/     PDF -> chapter.json / chapter.md / chapter.html
    code/                the pipeline (one script per step)
    agents/              agent briefs -- the prompts that read page images
    steps/*/out/         the agents' actual answers, per page
    data/                built chapters: JSON, Markdown, HTML, figures
    SPEC.md              the full specification and runbook
    LESSONS.md           every defect this pipeline has shipped, and the rule that stops it
  paper_extraction/      question papers -> structured questions
  ncert_to_paper_maps/   links a PYQ to the NCERT line it came from
  _shared/               registries shared across the three workflows
pyq_bank/                question-bank assembly
```

**Read `data_flow/ncert_extractions/LESSONS.md` before changing anything.** Every entry in it
is a real defect that reached a finished-looking file and was caught by a person reading it.

## What is NOT here, and how to get it

**Download the source files here:**
<https://drive.google.com/drive/folders/14MIr30o4M_IDyyXljjPhnRY2r-QD2Xlu?usp=sharing>

| missing | size | why | how to obtain |
|---|---|---|---|
| `source_pdfs/` | 766 MB | NCERT's copyright, not ours to redistribute | the Drive link above, or free from [ncert.nic.in](https://ncert.nic.in/textbook.php) — place at `data_flow/ncert_extractions/source_pdfs/{new,old}/class_{11,12}/{biology,chemistry,physics}/` |
| `steps/*/work/` + page PNGs | 2.5 GB | rendered from the PDFs; fully regenerable | produced automatically on the next run |
| `paper_extraction/papers/` | 1 GB | third-party question papers | the Drive link above |

After downloading, the directory layout must match the table above exactly — the pipeline
resolves a chapter id like `BIO11L-ch01` to a path, so a PDF in the wrong folder is simply
not found.

Everything else — all code, every agent brief, every agent answer, and the built chapters
with their figures — is committed.

## Running it

```bash
python3 -m venv .venv && .venv/bin/pip install pymupdf pillow numpy

# one chapter, end to end
.venv/bin/python code/run_chapter.py BIO11L-ch01

# what still needs an agent, and the check gate
.venv/bin/python code/run_step.py A2L --list --chapters BIO11L-ch01
.venv/bin/python code/check_chapter.py --all
```

Chapter ids are `{SUBJECT}{CLASS}{EDITION}-ch{NN}` — `BIO11L-ch01` is Class 11 Biology,
latest edition, chapter 1; `O` is the older pre-rationalisation edition.

**Use the virtualenv's Python, never the system `python3`.** The system interpreter on macOS
is 3.6 with an ASCII default and silently truncates these files at the first non-ASCII byte.

## The two renderers

One `chapter.json` produces both, and they stay in step because they read the same boxes:

| | `chapter.html` | `chapter-exact.html` |
|---|---|---|
| lays out by | reflowing the semantic tree | placing every measured box |
| good for | reading, search, translation, citing a paragraph | looking exactly like the printed book |
| can drift | yes — reflow depends on the reader's font metrics | no — nothing is laid out, only placed |

## CDN assets

Figures carry three fields: `image` (CDN URL), `image_local` (the path in this repo) and
`image_sha256`. Every consumer prefers the URL and falls back to the local file, so the repo
works offline. To re-upload after a re-extraction:

```bash
python code/cdn_login.py --phone <number>            # sends an OTP
python code/cdn_login.py --phone <number> --otp 1234 # prints the export lines
export ARIVIHAN_TOKEN=...  ARIVIHAN_USER_ID=...
python code/upload_assets.py --chapter BIO11L-ch01
python code/rerender.py BIO11L-ch01
```

**The order matters: build → upload → rerender.** `run_chapter.py` rebuilds the tree from the
PDF, so running it after an upload used to discard every URL. It now carries them forward by
SHA, but `rerender.py` is the correct way to refresh the outputs without rebuilding.

No credential is ever written to disk. `upload_assets.py` reads the token from the environment
only, and `.gitignore` blocks `.env`, `*.pem`, `*.key` and `cdn.json`.
