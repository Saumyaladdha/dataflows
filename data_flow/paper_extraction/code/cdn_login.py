#!/usr/bin/env python3
"""Get a CDN bearer token, so `upload_paper_assets.py` can run.

    python code/cdn_login.py --phone 7489451099            # sends the OTP
    python code/cdn_login.py --phone 7489451099 --otp 1234 # prints the export lines

Then:

    export ARIVIHAN_TOKEN=...  ARIVIHAN_USER_ID=...
    python code/run_chapter.py BIO11L-ch01 --upload

WHY THIS IS A SEPARATE SCRIPT
-----------------------------
The token is a short-lived bearer for a real staging account. It must never be written into
this repo -- committed once it is in the history for good, and anyone with a clone can upload
as that user. So this script PRINTS the export lines and writes nothing: the value lives in
your shell for as long as the shell lives, and nowhere else.

The auth endpoint was not recorded anywhere in this codebase -- only the upload URL was -- so
the candidates below are tried in order against the same host and the one that answers is
reported. If none answers, the script says exactly what it tried rather than guessing.
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

HOST = "https://platform-stage.arivihan.com"

# MEASURED, not guessed. The auth service sits beside the upload path under the same gateway:
# `/internal-metrics/auth/send-otp` answers `{"success":true,"message":"OTP sent successfully"}`
# for `{"phoneNumber": "<10 digits>"}`. Every other candidate returns a Tomcat 404 HTML page,
# and the number must be the bare 10 digits -- "+917489451099" gets "User with phone number
# not exists". The alternatives are kept so a changed gateway reports what it tried.
SEND = [
    "/internal-metrics/auth/send-otp",
    "/user-service/auth/send-otp",
    "/auth/send-otp",
    "/api/v1/auth/send-otp",
]
VERIFY = [p.replace("send-otp", "verify-otp") for p in SEND]


def _post(url, payload, timeout=20):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode("utf-8", "replace")


def _try(paths, payload):
    """(path, body) for the first endpoint that does not 404, else (None, report)."""
    tried = []
    for p in paths:
        url = HOST + p
        try:
            status, body = _post(url, payload)
            return url, body
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:200]
            tried.append(f"  {e.code:>3} {url}  {body}")
            # A 400/401 means the endpoint EXISTS and disliked the payload -- that is the one.
            # 400/401/403/422 means the endpoint EXISTS and disliked the payload; 500 can be
            # a transient send failure on an endpoint that is otherwise correct. A 404 is the
            # only answer that means "wrong path".
            if e.code in (400, 401, 403, 422, 500):
                return url, body
        except Exception as e:                                   # noqa: BLE001
            tried.append(f"  ERR {url}  {type(e).__name__}: {e}")
    return None, "\n".join(tried)


def _set_host(h):
    global HOST
    HOST = h.rstrip("/")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phone", required=True)
    ap.add_argument("--otp", help="the code you received; omit to request one")
    ap.add_argument("--host", default=HOST)
    a = ap.parse_args()
    _set_host(a.host)

    if not a.otp:
        url, body = _try(SEND, {"phoneNumber": a.phone})
        if not url:
            raise SystemExit(f"no send-otp endpoint answered. Tried:\n{body}\n\n"
                             f"Pass the right one with --host, or send the OTP yourself and "
                             f"re-run with --otp.")
        print(f"OTP requested via {url}\n{body[:300]}\n\n"
              f"Now run:  python code/cdn_login.py --phone {a.phone} --otp <code>")
        return

    url, body = _try(VERIFY, {"phoneNumber": a.phone, "otp": a.otp})
    if not url:
        raise SystemExit(f"no verify-otp endpoint answered. Tried:\n{body}")
    try:
        data = json.loads(body)
    except ValueError:
        raise SystemExit(f"{url} did not return JSON:\n{body[:400]}")

    def dig(d, *names):
        if isinstance(d, dict):
            for k, v in d.items():
                if k.lower() in names and isinstance(v, (str, int)):
                    return str(v)
            for v in d.values():
                got = dig(v, *names)
                if got:
                    return got
        elif isinstance(d, list):
            for v in d:
                got = dig(v, *names)
                if got:
                    return got
        return None

    token = dig(data, "token", "accesstoken", "access_token", "jwt", "idtoken")
    user = dig(data, "userid", "user_id", "id", "_id")
    if not token:
        raise SystemExit(f"verified, but no token field found in:\n"
                         f"{json.dumps(data, indent=1)[:600]}")
    print("# paste these into the shell you will run the upload from:")
    print(f"export ARIVIHAN_TOKEN='{token}'")
    if user:
        print(f"export ARIVIHAN_USER_ID='{user}'")
    else:
        print("# ARIVIHAN_USER_ID not found in the response -- set it yourself")
    print("\n# then:\n#   python code/run_chapter.py BIO11L-ch01 --upload"
          "\n#   python code/run_chapter.py BIO12L-ch01 --upload --allow-unmeasured")


if __name__ == "__main__":
    main()
