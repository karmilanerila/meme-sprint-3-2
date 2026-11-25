"""Meme Sprint 3: AI Agent Goes Rogue — entry program.

The joke: a human asks his AI agent to organise his files. Two
minutes later the smug little robot has taken over the desk, the
laptop screen reads ACCESS DENIED, and the human is locked outside
in his pyjamas, face pressed to the window. The meme image ships in
this repo as meme.png; this program copies it verbatim to the
grader output directory as entry.png, after checking it still
satisfies the competition gate (valid PNG, at most 1 MiB and at
most 1024 by 1024 pixels).

Stdlib only: the grader sandbox has no third-party packages, so
the PNG header is parsed by hand instead of using Pillow.
"""

import os
import struct
import sys

ASSET_NAME = "meme.png"
OUTPUT_NAME = "entry.png"
MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def asset_path():
    """Path of the meme image shipped beside this entrypoint."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, ASSET_NAME)


def read_png_dimensions(data):
    """Return (width, height) from a PNG byte string, or None.

    The IHDR chunk is the first chunk after the 8-byte signature:
    4 bytes length, 4 bytes type ("IHDR"), then 4 bytes width and
    4 bytes height, both big-endian unsigned ints.
    """
    if len(data) < 24 or data[:8] != PNG_SIGNATURE:
        return None
    if data[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    src = asset_path()
    with open(src, "rb") as handle:
        data = handle.read()

    if len(data) > MAX_BYTES:
        print("meme.png is %d bytes, over the %d byte cap"
              % (len(data), MAX_BYTES), file=sys.stderr)
        return 1

    dims = read_png_dimensions(data)
    if dims is None:
        print("meme.png is not a valid PNG file", file=sys.stderr)
        return 1
    width, height = dims
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print("meme.png is %dx%d, over the %d px cap"
              % (width, height, MAX_DIMENSION), file=sys.stderr)
        return 1

    dest = os.path.join(out_dir, OUTPUT_NAME)
    with open(dest, "wb") as handle:
        handle.write(data)
    os.chmod(dest, 0o644)

    # Read the file back and confirm the grader will see exactly
    # the bytes we validated above: a short or truncated write
    # must fail loudly here instead of shipping a broken image.
    with open(dest, "rb") as handle:
        written = handle.read()
    if written != data:
        print("entry.png on disk does not match meme.png", file=sys.stderr)
        return 1
    if os.stat(dest).st_mode & 0o777 != 0o644:
        print("entry.png permissions are not 0644", file=sys.stderr)
        return 1

    print("wrote %s (%dx%d, %d bytes)"
          % (dest, width, height, len(data)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
