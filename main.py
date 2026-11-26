#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun entry.

Writes one funny remark in the voice of a smug, judgmental
self-checkout machine to /output/entry.txt.

The line: a shopper with one banana and four energy drinks gets
the machine's verdict on how the night is going to go.
"""

import os

ENTRY = "One banana. Four energy drinks. We both know how tonight ends."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
