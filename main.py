#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

The text is reproduced byte for byte, with no trailing newline.
"""

import os
import sys

TEXT = (
    "For three years my father called the dog by my name. "
    "The dog has been dead since 2019. I answer anyway."
)


def output_dir() -> str:
    """Return the folder that receives entry.txt."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    data = TEXT.encode("utf-8")
    folder = output_dir()
    os.makedirs(folder, exist_ok=True)

    with open(os.path.join(folder, "entry.txt"), "wb") as handle:
        handle.write(data)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
