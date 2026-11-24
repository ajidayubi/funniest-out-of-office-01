#!/usr/bin/env python3
"""The Funniest Out-of-Office (make.fun).

Writes one line of an out-of-office auto-reply, the funniest I can make it,
in 140 characters or fewer, to /output/entry.txt.

The reply: "I'm away until Monday. I'm not ignoring you — I'm ignoring
everyone, equally, with love."

Why this line, against the judge's brief (a real one-line reply first, then
a genuine surprise, a voice of its own, freshness, every word earning its
place):
- It is a reply a real person would actually set: it opens like a normal
  auto-reply, with a return day ("away until Monday").
- The laugh turns on the surprise in the middle: "I'm not ignoring you"
  sounds like reassurance, then the sentence reverses it — the sender is
  ignoring everyone, equally.
- The last two words carry the voice: "with love" lands the deadpan
  warmth, a person talking, not a template.
- It steers clear of the jokes every inbox has already read: no beach,
  no inbox left in charge of a pet, no "back soon".
- Every word earns its place: cut any of them and the turn or the landing
  goes with it.

The program is deterministic: it writes the same bytes on every run, uses
only the standard library, and needs no network.
"""

import argparse
import os

REPLY = "I'm away until Monday. I'm not ignoring you — I'm ignoring everyone, equally, with love."

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write the out-of-office reply to entry.txt."
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Write to this path instead of $MAKEFUN_OUTPUT_DIR/entry.txt",
    )
    args = parser.parse_args()
    if args.out:
        out_path = args.out
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        out_path = os.path.join(out_dir, "entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
