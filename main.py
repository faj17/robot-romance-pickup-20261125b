#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — make.fun entry.

Writes one original pickup line, written to charm a robot or an AI,
to /output/entry.txt (1-200 characters, UTF-8, a single line).
Standard library only, no network, no input.

The line is built from two fragments: a setup (the speaker addresses
a CAPTCHA — the machine that decides whether you are human) and a
punch (the turn: the speaker keeps failing it on purpose, not to get
past the gate but to stay on the page with it). ``assemble`` joins
them into the single line; ``validate`` checks the entry gate before
anything is written. The machine premise is the whole flirt: failing
the test is the proof of interest, and "proving I'm not a robot"
flips into wanting to linger with the machine that asks.
"""

from pathlib import Path

SETUP = "Are you a CAPTCHA?"
PUNCH = "Because I keep failing you on purpose just to stay on this page with you."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one pickup line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    line.encode("utf-8")
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
