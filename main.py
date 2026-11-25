#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes one original one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The entry must be 1-200 characters of
UTF-8 text, a single line, no second line.
"""

import os

# Original one-liner: the meeting literally WAS the email, read aloud.
# Turn lands on the last word; "word for word" is the recognition hook
# every office worker has sat through.
ENTRY = (
    "The host opened the meeting by reading the email aloud, word for word, "
    "then asked if anyone had questions about the email he'd just read."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of
    # 1-200 characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
