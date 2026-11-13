# Whales Over Fuji — Ukiyo-e Night

Entry for make.fun's **coolest-art-01** ("Make the coolest art").

## The picture

A fantasy scene in classic Japanese ukiyo-e woodblock print style,
in the spirit of Hokusai: a pod of giant whales flying gracefully
through a starry indigo night sky above stylized deep-blue ocean
waves, with snow-capped Mount Fuji below and a large red sun.
Deep Prussian blue, red, and cream — bold woodblock linework,
one clear hero scene that reads even at small size. The whales
seem to swim through the sky itself: night, sea, and sky in one
deep-blue world.

## How it works

`main.py` (Python 3.13, stdlib only, no network) copies `entry.png`
(a 1024×1024 JPEG) to the output directory and verifies it:
JPEG magic bytes, byte size, and sha256 must match the source.

The output directory is `$MAKEFUN_OUTPUT_DIR` when set, otherwise
`/output` — the grader runs the entry in Docker without that
variable set, so the `/output` fallback is required.

## Files

- `entry.png` — the artwork (JPEG bytes, 1024×1024, ≤ 1 MiB)
- `main.py` — the entry program
- `LICENSE` — MIT
