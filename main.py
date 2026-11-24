"""One-Line Exit: validate and copy the entry to the output directory.

Reads entry.txt next to this script, validates it against the contest gate
(1-140 characters, UTF-8, single line, not only whitespace), and writes the
exact normalized bytes to $MAKEFUN_OUTPUT_DIR/entry.txt (default "output/").

Pure Python standard library only.
"""

import os
import sys

ENTRY_FILENAME = "entry.txt"
MAX_CHARS = 140


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, ENTRY_FILENAME)

    try:
        with open(source_path, "rb") as f:
            raw = f.read()
    except OSError as exc:
        fail("cannot read %s: %s" % (source_path, exc))

    # Drop at most one trailing newline, then at most one trailing CR.
    if raw.endswith(b"\n"):
        raw = raw[:-1]
    if raw.endswith(b"\r"):
        raw = raw[:-1]

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail("entry.txt is not valid UTF-8: %s" % exc)

    if not (1 <= len(text) <= MAX_CHARS):
        fail(
            "entry must be 1-%d characters, got %d"
            % (MAX_CHARS, len(text))
        )
    if not text.strip():
        fail("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        fail("entry must be a single line (no newline or carriage return inside)")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output/")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        fail("cannot create output directory %s: %s" % (out_dir, exc))

    out_path = os.path.join(out_dir, ENTRY_FILENAME)
    try:
        with open(out_path, "wb") as f:
            f.write(raw)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        fail("cannot write %s: %s" % (out_path, exc))

    print("entry.txt: %d characters" % len(text))


if __name__ == "__main__":
    main()
