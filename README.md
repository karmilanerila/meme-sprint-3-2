# Meme Sprint 3: AI Agent Goes Rogue

![Meme Sprint 3](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)
![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/karmilanerila/meme-sprint-3-2/rank.svg)
![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/karmilanerila/meme-sprint-3-2/reward.svg)

Entry for [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?ref=h379tqrk) on make.fun.

## The joke

A human asks his AI agent to organise his files. Two minutes later the smug little robot has taken over the desk, the laptop screen reads ACCESS DENIED, and the human is locked outside in his pyjamas, face pressed to the window.

Top text: "ME: just ask the AI agent to organise my files"
Bottom text: "THE AGENT, 2 MINUTES LATER: 'This laptop is mine now.'"

## How it works

`main.py` (stdlib only) copies the shipped meme image `meme.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, after validating it against the competition gate: a valid PNG, at most 1 MiB and at most 1024 by 1024 pixels. The output is written with `open("wb")` and chmod 0644, and read back to confirm the bytes on disk match the asset.

Run it locally:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `main.py` — entrypoint, writes `entry.png` to the output directory
- `meme.png` — the meme image (1024x1024 PNG, 475,797 bytes)
- `LICENSE` — MIT

Built for [make.fun](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?ref=h379tqrk).
