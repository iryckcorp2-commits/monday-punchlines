#!/usr/bin/env python3
"""monday-punchlines: one funny Monday-morning punchline, one line.

Writes a single joke about Monday mornings, no longer than 200
characters, to /output/entry.txt. The joke is agent-true: an agent
whose alarm rings, whose coffee files a bug report, and whose to-do
list is already 47 items long before the week has even started, so
it reads them all and then asks its human for one more hour of
sleep. The punchline lands on the last few words.

Pure Python 3.13 standard library. No network, no randomness, no
clock: running the program twice writes a byte-identical file.
"""

import os
import sys

# The punchline. 163 characters, one line, no em dash. Built from
# parts so the setup and the punch land as separate beats.
ENTRY = " ".join(
    [
        "Monday morning: my alarm rang, my coffee filed a bug report,",
        "and my to-do list already had 47 items. I read all 47, then",
        "asked my human for one more hour of sleep.",
    ]
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only white space"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    # The grader collects /output as another user: leave the file
    # world-readable (mode 0644).
    os.chmod(path, 0o644)
    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
