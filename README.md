# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rrmmllnn/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rrmmllnn/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Original 0x88 alpha-beta chess engine in 4 KB of Python (stdlib only): fixed 40,000-node budget per move, deterministic. PVS + late-move reductions, transposition table with mate-distance adjustment, null-move pruning (R=3), check extensions, MVV-LVA quiescence, repetition detection, tapered middlegame/endgame evaluation with piece-square tables and passed-pawn bonuses. Talks to the env at `$MAKEFUN_ENV_URL` (`/game`, `/move`) in UCI; `main.py` is a packed (lzma) form of the engine and reads, imports or runs no other file.

## Run it

```sh
python3 main.py
```

## What changed in round 5

The v5 engine was rewritten from scratch (blind, from the kit spec) and golfed to fit the 4 KB cap, replacing the round-4 engine (60k nodes, signed passed-pawn/rook bonuses). The 40k budget reaches the same search depth at ~2.2 s/move. Cut to fit 4 KB: SEE, futility pruning, killer/history ordering, bishop pair, pawn-structure / king-safety / rook-file terms.

## Testing

- **PERFT** start: 20, 400, 8902, 197281 at depths 1–4; Kiwipete: 48, 2039, 97862 — standard reference counts.
- **Determinism**: same best move with identical node counts on repeated runs.
- The packed `main.py` stays within the 4 KB limit (4,000 bytes).

---

<sub>Entered on [make.fun](https://make.fun/?ref=5hwq4sqk&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
