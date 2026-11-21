#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes a single one-line joke about working beside AI coding agents
to /output/entry.txt (or $OUTPUT_PATH when set for local testing).

The joke is a fixed, hand-written string: the program is deterministic,
uses no network, and writes exactly one line of UTF-8 text.
"""

import os
from pathlib import Path

JOKE = (
    "Live on stage, my coding agent apologised for the crash, "
    "fixed it, then proudly reintroduced it as a feature."
)

MIN_LENGTH = 1
MAX_LENGTH = 280
DEFAULT_OUTPUT = "/output/entry.txt"


def validate_joke(text: str) -> str:
    """Return the joke unchanged if it satisfies the entry rules.

    Rules (from the competition kit): 1-280 Unicode code points,
    not only whitespace, and exactly one line.
    """
    if not isinstance(text, str):
        raise TypeError("joke must be a string")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"joke must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        raise ValueError("joke must not contain control characters")
    return text


def output_path() -> Path:
    """Resolve where entry.txt goes: $OUTPUT_PATH or /output/entry.txt."""
    return Path(os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT))


def render() -> str:
    """Build the entry text (the joke, validated)."""
    return validate_joke(JOKE)


def write_entry(path: Path | None = None) -> Path:
    """Write the validated joke to entry.txt and return its path."""
    target = path or output_path()
    text = render()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return target


def main() -> None:
    target = write_entry()
    print(f"Wrote {len(render())} characters to {target}")


if __name__ == "__main__":
    main()
