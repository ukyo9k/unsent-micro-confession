#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun entry.

Writes one two-part micro-confession (a To: line naming who it was
meant for, plus the unsent message itself, one line exactly as typed)
to /output/entry.txt.

The entry is fixed text: the confession was typed once and never sent,
so the program writes it deterministically, byte for byte, every run.
"""

import os
import sys

ENTRY = (
    "To: the nurse on the night shift, Ward 4B\n"
    "You held my hand while my mother died and I never learned your name, "
    "so I never got to thank you.\n"
)


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Verification guard: re-read what was written and enforce the
    # competition gate before reporting success, so a truncated or
    # non-UTF-8 write can never pass silently.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("error: entry.txt does not match the intended text", file=sys.stderr)
        return 1
    if not (1 <= len(written) <= 260) or not written.strip():
        print("error: entry.txt outside the 1-260 character gate", file=sys.stderr)
        return 1
    lines = written.rstrip("\n").split("\n")
    if len(lines) != 2 or not lines[0].startswith("To: "):
        print("error: entry must be a To: line plus one message line", file=sys.stderr)
        return 1
    if len(lines[1]) > 200:
        print("error: message line exceeds 200 characters", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
