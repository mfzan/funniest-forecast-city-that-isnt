#!/usr/bin/env python3
"""Funniest forecast for a city that isn't.

Writes one line -- a weather bulletin for the invented city of
Plot Hole City -- to /output/entry.txt (or $OUTPUT_PATH when set).
Standard library only, fully deterministic: the same line every run.
"""

import os

MAX_CHARS = 120

ENTRY_LINE = (
    "Today in Plot Hole City: 100% chance of plot holes, "
    "with scattered continuity errors by afternoon."
)


def main():
    os.umask(0o022)

    line = ENTRY_LINE.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            "entry line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )

    out_path = os.environ.get("OUTPUT_PATH") or "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # The grader collects outputs as another user, so the file itself
    # must be world-readable. Never chmod the /output directory: it is
    # root-owned and chmod on it fails the run.
    os.chmod(out_path, 0o644)
    # Prove the write landed whole: read it back and compare against
    # the line that passed validation, byte for byte.
    with open(out_path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line:
        raise SystemExit("output file does not match the validated line")


if __name__ == "__main__":
    main()
