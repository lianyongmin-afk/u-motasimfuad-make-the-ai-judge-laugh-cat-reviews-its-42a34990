#!/usr/bin/env python3
"""Cat Reviews Its Human — one-star review entry for make.fun.

Writes a single funny one-star review, written by a house cat about
its human, to /output/entry.txt. Deterministic: same bytes every run.
Stdlib only, no network.
"""

import os

LINE = (
    "One star. At 3 AM I brought Dave a mouse, a gift. "
    "He screamed, threw it away, and bought a $30 toy mouse "
    "that squeaks. I have stopped giving. "
    "He wonders why I am distant."
)


def main() -> None:
    text = LINE + "\n"
    # Gate: entry must be 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be whitespace-only"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
