#!/usr/bin/env python3
"""news-image-20261120 entry: sum up Friday 20 November 2026's world news in one image.

The program copies the bundled front-page image (entry.png, 1024x1024, drawn
from real reporting of 20 Nov 2026: the first-ever Trump-Xi-Putin trilateral
summit, Ukraine's third Crimea Bridge strike of the week, tankers ablaze near
Hormuz, the World Court's Myanmar genocide ruling, the Senate vote to release
the Epstein files, Wall Street's slide as Anthropic's IPO fizzles, and Bitcoin
under $62,000) to /output/entry.png.

Standard library only, no network, fully deterministic: the same bundled bytes
are copied on every run.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard the gate: the output must be a whole PNG, so check its signature.
    with open(dst, "rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            raise SystemExit("entry.png is not a PNG file")
    print(f"copied {src} -> {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
