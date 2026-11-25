#!/usr/bin/env python3
"""
Entry for "The Meeting That Should Have Been an Email" competition.
Writes the joke line to entry.txt, verifies it, and prints character count.
"""
import os
import sys

# The exact line to write (102 characters)
ENTRY_LINE = "This meeting could have been an email, but the email would have needed a meeting to explain the email."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")

    # Write the line (exactly one line, no extra newlines beyond the single line)
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)

    # Read it back and verify
    with open(entry_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Assert it matches exactly
    assert content == ENTRY_LINE, f"Content mismatch:\nExpected: {repr(ENTRY_LINE)}\nGot: {repr(content)}"

    # Print character count
    print(f"Wrote {len(ENTRY_LINE)} characters to {entry_path}")

if __name__ == "__main__":
    main()