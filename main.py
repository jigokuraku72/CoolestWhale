#!/usr/bin/env python3
"""Whales Over Fuji — coolest-art-01 entry.

Copies entry.png (a ukiyo-e style scene: whales flying through a
starry indigo night sky above stylized blue waves, Mount Fuji below,
a large red sun) to the output directory.

Stdlib only, no network. The output directory is $MAKEFUN_OUTPUT_DIR
when set, otherwise /output (the grader's Docker container does not
set MAKEFUN_OUTPUT_DIR, it mounts the output dir at /output).
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")

    with open(SRC, "rb") as f:
        magic = f.read(2)
    if magic != b"\xff\xd8":
        print("error: entry.png is not a JPEG", file=sys.stderr)
        return 1

    shutil.copyfile(SRC, dst)

    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        print("error: size mismatch", file=sys.stderr)
        return 1

    src_sha = sha256_of(SRC)
    dst_sha = sha256_of(dst)
    if src_sha != dst_sha:
        print("error: sha256 mismatch", file=sys.stderr)
        return 1

    print(f"wrote {dst} ({dst_size} bytes, JPEG magic OK)")
    print(f"sha256 source={src_sha}")
    print(f"sha256 output={dst_sha} (match)")
    print(f"verified: {dst_size} bytes, sha256 {dst_sha[:12]}... matches source")
    return 0


if __name__ == "__main__":
    sys.exit(main())
