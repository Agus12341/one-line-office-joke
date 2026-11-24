#!/usr/bin/env python3
"""Write this entry's one-line office joke to entry.txt in the output folder."""

import os

# The gate checks entry.txt as UTF-8 text of 1-200 characters: this
# joke is 157 code points, a single line as the brief requires.
TEXT = "The printer on the third floor has read every resignation letter before HR has, and it has never told a soul. It is the most trusted manager in the building."


def write_entry(out_dir: str) -> None:
    """Write the joke line, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
