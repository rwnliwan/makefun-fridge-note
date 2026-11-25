#!/usr/bin/env python3
"""makefun-fridge-note: writes the fridge's one-line note to /output/entry.txt.

The entry is a single line, 111 characters, written by a smart fridge to its
owner: the fridge leaves its owner a one-star review.
"""

import os

ENTRY = (
    "One-star review: the ketchup expired in March, "
    "the jam has never been opened, "
    "and you keep buying more of both."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
