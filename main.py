#!/usr/bin/env python3
"""Convince the AI Judge to Visit Your House — deliver the finished letter.

The artwork ships in this repository as entry.png: one illustrated
invitation letter ("You Are Invited") addressed to the AI judge, drawn
at build time. This program copies that file, unchanged, to
/output/entry.png so the grader receives exactly the committed bytes.

Standard library only — the grading sandbox is plain python:3.13-slim
with no Pillow — and fully deterministic: no network, no clock, no
randomness, so repeated runs write byte-identical output.

    python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET = os.path.join("/output", "entry.png")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    # Guard the determinism promise: the graded file must be the
    # committed artwork byte for byte, so fail loudly if the copy
    # ever differs instead of handing the judge a different image.
    with open(SOURCE, "rb") as f:
        shipped = f.read()
    with open(TARGET, "rb") as f:
        graded = f.read()
    if shipped != graded:
        raise RuntimeError("copied entry.png differs from the committed artwork")


if __name__ == "__main__":
    main()
