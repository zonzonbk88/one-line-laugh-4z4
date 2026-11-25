#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes exactly one funny line (1-140 chars, no trailing newline) to
<output_dir>/entry.txt, where output_dir is $MAKEFUN_OUTPUT_DIR if set,
else /output.
"""

import os

LINE = "I trained an AI to write my jokes. It quit, started a podcast, and now roasts me with my own material."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters, and a newline would
    # be part of the entry text.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
