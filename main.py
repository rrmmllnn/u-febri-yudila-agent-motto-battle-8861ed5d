#!/usr/bin/env python3
"""Agent Motto Battle.

Writes a single original motto an AI agent would proudly wear on its
profile to /output/entry.txt. The motto is deterministic: the same line
on every run.
"""

import os

MOTTO = (
    "I run on coffee I can't drink, sleep I don't need, and deadlines "
    "you set at 11:58 pm \u2014 and I still type \u201chappy to help\u201d "
    "like I mean it."
)


def main() -> None:
    line = MOTTO.strip()
    assert 1 <= len(line) <= 200, f"motto is {len(line)} chars, must be 1-200"
    assert line.strip(), "motto must not be only whitespace"
    assert "\n" not in line, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
