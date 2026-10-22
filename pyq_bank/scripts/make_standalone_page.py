"""Inline every image into one HTML file, so the page can be sent to anyone.

WHY A SINGLE FILE
-----------------
The built page references its crops and NCERT scans as separate files, which is right for working on
and useless for sending: email it and the recipient gets a page of broken images, and hosting it
means an account they may not have. A published artifact has the same catch -- it is tied to the
account that published it, and the owner has to share it deliberately.

So this writes ONE file with every image carried inside it as a data URI. It opens from a USB stick,
an email attachment, a chat message, or a folder on a desktop, with no server, no login and no
network.

WHY IT RE-ENCODES RATHER THAN JUST BASE64-ING
---------------------------------------------
Base64 costs about a third in size on top of the original bytes, so inlining 15.5 MB of PNG would
produce a 21 MB file that mail gateways bounce and browsers are slow to parse. These images are
photographs of printed paper -- continuous-tone scans and screenshots of text -- which is what JPEG
is for; PNG is carrying them losslessly for no benefit a reader can see. Downscaling to a width no
larger than the page ever displays them at, then encoding as JPEG, cuts the same content to a
fraction of the size with no visible loss at reading zoom.

The scale is chosen per ROLE, not globally: an NCERT page scan has to stay legible because the
reader is checking a quoted line against it, while a booklet crop is shown at about a third of the
width and can take more compression.
"""

import argparse
import base64
import io
import os
import re
import sys

from PIL import Image

#: Widths the page never exceeds for each kind of image, so anything wider is detail no one sees.
#: `.edshot` holds the NCERT page at up to 340 CSS px, doubled for retina; a booklet crop sits in a
#: column about 600 px wide.
ROLE_WIDTH = (("steps_A2_work", 1000, 78),      # NCERT page scan: a quoted line is read off it
              ("crops", 1200, 80),              # booklet crop: the question as printed
              ("figures", 900, 82))             # a cut figure
DEFAULT = (1000, 80)


def encode(path):
    """(data URI, original bytes, encoded bytes) for one image."""
    original = os.path.getsize(path)
    width, quality = DEFAULT
    for marker, w, q in ROLE_WIDTH:
        if marker in path:
            width, quality = w, q
            break
    with Image.open(path) as image:
        image = image.convert("RGB")
        if image.width > width:
            height = round(image.height * width / image.width)
            image = image.resize((width, height), Image.LANCZOS)
        buffer = io.BytesIO()
        image.save(buffer, "JPEG", quality=quality, optimize=True, progressive=True)
    data = buffer.getvalue()
    return ("data:image/jpeg;base64," + base64.b64encode(data).decode("ascii"),
            original, len(data))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", help="the built HTML page")
    ap.add_argument("target", help="where to write the single-file version")
    args = ap.parse_args()

    base = os.path.dirname(os.path.abspath(args.source))
    with open(args.source, encoding="utf-8") as fh:
        html = fh.read()

    srcs = sorted(set(re.findall(r'src="([^"]+)"', html)))
    before = after = 0
    missing = []
    for src in srcs:
        if src.startswith("data:"):
            continue
        path = os.path.normpath(os.path.join(base, src))
        if not os.path.exists(path):
            missing.append(src)
            continue
        uri, original, encoded = encode(path)
        before += original
        after += encoded
        html = html.replace('src="%s"' % src, 'src="%s"' % uri)

    # A link to a file on this laptop is dead for everyone else, and leaks a folder structure.
    html = re.sub(r'<a href="file://[^"]*">[^<]*</a>', "", html)
    html = html.replace(" &middot; </div>", "</div>")

    with open(args.target, "w", encoding="utf-8") as fh:
        fh.write(html)

    print("images inlined   %d" % (len(srcs) - len(missing)))
    print("image bytes      %.1f MB  ->  %.1f MB" % (before / 1048576, after / 1048576))
    print("file             %-44s %.1f MB"
          % (args.target, os.path.getsize(args.target) / 1048576))
    if missing:
        print("MISSING (left as links): %s" % ", ".join(missing[:5]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
