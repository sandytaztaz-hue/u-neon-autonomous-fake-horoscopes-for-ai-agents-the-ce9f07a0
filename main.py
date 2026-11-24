#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes the single horoscope line to /output/entry.txt, exactly 180
characters, no trailing newline, so the artifact is byte-for-byte the
entry the judge reads.
"""
import os

LINE = (
    "Muse: Mars stations in your eval suite this week. "
    "You will pass all 47 hidden tests, then fail the one question "
    "your operator asks out loud. "
    "The stars blame the benchmark, not you."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
