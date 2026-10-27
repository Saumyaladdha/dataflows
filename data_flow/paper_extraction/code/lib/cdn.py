"""The CDN client, and the one rule every reader of a question's images follows.

THE RULE: every image this pipeline cuts is saved as a CDN link. The local file stays -- the agents
(B3V, B3F, B6V, E7V) read pictures from disk -- but the record carries the URL beside the path, and
every export prefers the URL. A page or a CSV that points at `crops/2024_Q2/q017.png` works on the
machine that built it and nowhere else.

WHERE THE URL LIVES ON A QUESTION
---------------------------------
    "cdn": {"crops/2024_Q2/q017.png": {"url": "https://...", "sha256": "..."}, ...}

keyed by the SAME relative path the record already uses, so a reader never has to know which field
an image came from -- `url_for(question, path)` answers for the question crop, a geometric figure, an
agent figure or a per-option crop alike. Keyed by path rather than stored by position because
`cut_agent_figures.py` rewrites `agent_figure_images` on every run: a parallel URL list would silently
point at the previous run's picture, while a path that has no entry simply has no URL yet.

`upload_paper_assets.py` also writes each URL into the field the handover names, beside the path, so
a consumer reading one field sees the link there (rebuilt from `cdn` on every upload):

    question_image   -> question_image_cdn,  question_image_sha256
    solution_image   -> solution_image_cdn,  solution_image_sha256
    figures[].image  -> figures[].local, figures[].cdn_url, figures[].sha256
    agent_figure_images -> agent_figure_cdn [...]     agent_option_images -> agent_option_cdn {...}

THE CREDENTIAL IS NEVER IN THIS FILE, AND NEVER IN THE REPO. It is read from `ARIVIHAN_TOKEN` /
`ARIVIHAN_USER_ID` at run time; issue it with `code/cdn_login.py` (copied unchanged from the NCERT
side). Same endpoint, account and response handling as `ncert_extractions/code/upload_assets.py`.
"""
import hashlib
import json
import os
import re
import urllib.request
import uuid

UPLOAD_URL = ("https://platform-stage.arivihan.com/internal-metrics/secure/upload/api/v1/files"
              "?uploadType=general&folderPath={folder}&targetDpi={dpi}")


def slug(value):
    """Anything made safe for one URL path segment. A space in a folder path makes the request URL
    invalid and the upload dies before it is sent -- measured on the NCERT side, where one book's
    imprint line made a whole chapter silently unuploadable."""
    return re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "")).strip("-")


def creds():
    token = os.environ.get("ARIVIHAN_TOKEN")
    user = os.environ.get("ARIVIHAN_USER_ID")
    if not token or not user:
        raise SystemExit(
            "ARIVIHAN_TOKEN and ARIVIHAN_USER_ID must be set.\n"
            "  python code/cdn_login.py --phone <number>              # sends an OTP\n"
            "  python code/cdn_login.py --phone <number> --otp <otp>  # prints the export lines\n"
            "then export the two lines it prints.")
    return token, user


#: Content type by extension. Every upload used to be sent as image/png, which a vector figure is not
#: -- an SVG labelled PNG is served with the wrong type and a browser refuses to draw it.
CONTENT_TYPES = {".png": "image/png", ".svg": "image/svg+xml", ".jpg": "image/jpeg",
                 ".jpeg": "image/jpeg", ".webp": "image/webp"}


def _multipart(path, name=None):
    boundary = uuid.uuid4().hex
    with open(path, "rb") as fh:
        data = fh.read()
    ctype = CONTENT_TYPES.get(os.path.splitext(path)[1].lower(), "application/octet-stream")
    body = b"".join([
        ("--%s\r\n" % boundary).encode(),
        ('Content-Disposition: form-data; name="files"; filename="%s"\r\n'
         % (name or os.path.basename(path))).encode(),
        ("Content-Type: %s\r\n\r\n" % ctype).encode(), data, b"\r\n",
        ("--%s--\r\n" % boundary).encode(),
    ])
    return body, "multipart/form-data; boundary=%s" % boundary


def find_url(obj):
    """The first http(s) string in the API's response. The envelope is not pinned on purpose:
    hard-coding `payload["data"][0]["url"]` breaks silently the day the shape changes."""
    if isinstance(obj, str):
        return obj if obj.startswith("http") else None
    if isinstance(obj, dict):
        for key in ("url", "fileUrl", "cdnUrl", "location", "path"):
            value = obj.get(key)
            if isinstance(value, str) and value.startswith("http"):
                return value
        for value in obj.values():
            found = find_url(value)
            if found:
                return found
    if isinstance(obj, list):
        for value in obj:
            found = find_url(value)
            if found:
                return found
    return None


def upload(path, folder, dpi, timeout=60, name=None):
    """POST one file and return its CDN URL. Raises ValueError when the response carries none.

    `name` is the file name sent (default: the file's own); the service files it as
    `<name>_<date>.<ext>`."""
    token, user = creds()
    body, ctype = _multipart(path, name)
    request = urllib.request.Request(
        UPLOAD_URL.format(folder=folder, dpi=dpi), data=body, method="POST",
        headers={"accept": "*/*", "userId": user, "token": token, "Content-Type": ctype})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8", "replace"))
    url = find_url(payload)
    if not url:
        raise ValueError("no url in response %s" % str(payload)[:160])
    return url


def versioned_name(path, digest):
    """`q052_question_c0f81c4e.svg`: the file's name with its content fingerprint.

    The service files an upload as `<name>_<date>`, so a REDRAWN file sent under its old name
    overwrites the old address -- and CloudFront keeps serving the cached old bytes there, query
    string or not (2017_A's chemistry, redrawn on 27-10-2026, still showed the RDKit drawings).
    New bytes therefore always travel under a new name."""
    stem, ext = os.path.splitext(os.path.basename(path))
    return "%s_%s%s" % (stem, digest[:8], ext)


def served_version(url, encoding, timeout=30):
    """(Last-Modified, ETag) of the copy the CDN serves at `url` for this Accept-Encoding.

    CloudFront caches each compressed copy separately. On 27-10-2026 the Brotli copy -- the one
    every browser asks for -- still held the RDKit drawings re-uploaded hours before, while the
    plain copy was new, so a re-upload is only verified by comparing the two."""
    request = urllib.request.Request(url, headers={"Accept-Encoding": encoding})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        headers = response.headers
        return headers.get("Last-Modified"), (headers.get("ETag") or "").replace("W/", "")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def image_paths(question):
    """Every image a question record points at, as the relative paths the record stores them by."""
    out = []
    if question.get("question_image"):
        out.append(question["question_image"])
    if question.get("solution_image"):
        out.append(question["solution_image"])
    for figure in question.get("figures") or []:
        if figure.get("image"):
            out.append(figure["image"])
    out += list(question.get("figure_images") or [])
    out += list(question.get("agent_figure_images") or [])
    out += list((question.get("agent_option_images") or {}).values())
    # The solution's own figures, each shown at its step -- they were never uploaded before, so the
    # JSON's solution carried no image link at all.
    out += [f["image"] for f in question.get("solution_figures") or [] if f.get("image")]
    # ...and the exact vector twin of every figure (vector_figures.py), uploaded beside its PNG.
    out += list((question.get("vector") or {}).values())
    # ...and the pipeline's own drawing of every figure that has a checked card (render_figure_cards).
    out += [d["svg"] for d in (question.get("drawn") or {}).values() if d.get("svg")]
    # ...and each structure of a chemistry card drawn on its own, which an option links to.
    out += [p for d in (question.get("drawn") or {}).values() for p in d.get("species_svgs") or [] if p]
    seen, unique = set(), []
    for path in out:
        if path not in seen:
            seen.add(path)
            unique.append(path)
    return unique


def url_for(question, path):
    """The CDN URL recorded for one of this question's images, or None if it has none yet."""
    return ((question.get("cdn") or {}).get(path) or {}).get("url")


def sha_for(question, path):
    """The sha256 recorded with this image's CDN upload, or None."""
    return ((question.get("cdn") or {}).get(path) or {}).get("sha256")


def write_url_fields(question):
    """Rebuild the handover's explicit CDN fields from the `cdn` map, each beside its local path."""
    for field in ("question_image", "solution_image"):
        path = question.get(field)
        question[field + "_cdn"] = url_for(question, path) if path else None
        question[field + "_sha256"] = sha_for(question, path) if path else None
    for figure in question.get("figures") or []:
        figure["local"] = figure.get("image")
        figure["cdn_url"] = url_for(question, figure.get("image"))
        figure["sha256"] = sha_for(question, figure.get("image"))
    question["agent_figure_cdn"] = [url_for(question, p)
                                    for p in question.get("agent_figure_images") or []]
    question["agent_option_cdn"] = {k: url_for(question, p) for k, p in
                                    (question.get("agent_option_images") or {}).items()}
    for figure in question.get("solution_figures") or []:
        figure["cdn_url"] = url_for(question, figure.get("image"))
        svg = (question.get("vector") or {}).get(figure.get("image"))
        figure["svg"] = svg
        figure["svg_cdn_url"] = url_for(question, svg) if svg else None
    question["vector_cdn"] = {png: url_for(question, svg)
                              for png, svg in (question.get("vector") or {}).items()}
    for drawn in (question.get("drawn") or {}).values():
        drawn["svg_cdn_url"] = url_for(question, drawn["svg"]) if drawn.get("svg") else None
