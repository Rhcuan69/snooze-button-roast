#!/usr/bin/env python3
"""Snooze Button Roast entry.

Writes exactly one line roasting an alarm clock that rings at 6 AM on a
Saturday, to /output/entry.txt. Pure Python stdlib, deterministic: every run
produces byte-identical output.
"""

import os

LINE = (
    "My alarm clock rang at 6 AM on a Saturday like a coworker who "
    "volunteers for the weekend shift just to prove it has no life either."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
