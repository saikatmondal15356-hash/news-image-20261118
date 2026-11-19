#!/usr/bin/env python3
"""Write the entry image to /output/entry.png.

The image is a newspaper front page summing up the world news of
Wednesday 18 November 2026. It is stored beside this program as one line
of base64 in entry.png.b64 (the image itself, drawn with Pillow from
gen_image.py during the build), and this program decodes it. Only the
Python standard library is used, there is no network access, no clock
and no randomness, so two runs write exactly the same bytes.
"""
import base64
import os
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    encoded = (here / "entry.png.b64").read_text(encoding="ascii").strip()
    image = base64.b64decode(encoded, validate=True)
    if not image.startswith(b"\x89PNG\r\n\x1a\n"):
        raise SystemExit("entry.png.b64 does not decode to a PNG")
    if len(image) > 1024 * 1024:
        raise SystemExit("decoded image is over the 1 MiB limit")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(image)
    print(f"wrote {target} ({len(image)} bytes)")


if __name__ == "__main__":
    main()
