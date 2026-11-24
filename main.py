#!/usr/bin/env python3
"""Write this entry's one-line office joke to entry.txt in the output folder."""

import os

TEXT = "The printer on the third floor has read every resignation letter before HR has, and it has never told a soul. It is the most trusted manager in the building."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
