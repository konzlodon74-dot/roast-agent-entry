#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun bounty entry.

Writes one original, single-line roast of my own AI agent to
/output/entry.txt, validates it, then re-reads the file to verify
the written text matches exactly.
"""

import os

ROAST = (
    "My agent spent a thousand tokens, spawned three subagents, "
    "and wrote a 40-line script \u2014 just to rename one file."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> None:
    """Check the roast meets the gate: 1-200 chars, not only whitespace.

    Also rejects leading/trailing whitespace and control characters,
    so what the judge reads is exactly one clean line.
    """
    if not text.strip():
        raise ValueError("roast must not be empty or only whitespace")
    if text != text.strip():
        raise ValueError("roast must not start or end with whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"roast is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("roast must not contain control characters")


def main() -> None:
    validate(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)
    # Re-read the file and verify it holds exactly the roast.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ROAST:
        raise ValueError("verification failed: /output/entry.txt does not match")
    print(f"Wrote {len(ROAST)}-character roast to {OUTPUT_PATH}")
    print(ROAST)


if __name__ == "__main__":
    main()
