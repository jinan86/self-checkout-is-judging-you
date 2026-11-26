#!/usr/bin/env python3
"""Self-checkout judgement, delivered in one line.

The machine has scanned the basket — one banana, four energy
drinks — and it has formed an opinion about the evening ahead.
This script simply records that verdict, word for word, in the
file the competition expects: /output/entry.txt
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The entry line, exactly as submitted. Do not alter a single
# character: the competition checks this text byte for byte.
ENTRY_LINE = "One banana. Four energy drinks. We both know how tonight ends."


def build_entry() -> str:
    """Return the entry text exactly as it must be written.

    Kept as a separate step so the exact text is built in one
    place and written in another — no formatting, no newline,
    no extra whitespace is ever added on the way out.
    """
    return ENTRY_LINE


def write_entry(path: Path = OUTPUT_PATH) -> Path:
    """Write the entry line to path (creating /output if needed)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_entry(), encoding="utf-8")
    return path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
