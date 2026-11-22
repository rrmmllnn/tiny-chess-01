# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rrmmllnn/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rrmmllnn/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Original 0x88 alpha-beta chess engine in 4 KB of Python (stdlib only): fixed 40,000-node budget per move, deterministic, with PVS + late-move reductions, transposition table with mate-distance adjustment, null-move pruning, check extensions, MVV-LVA quiescence, repetition detection, and a tapered middlegame/endgame evaluation with piece-square tables and passed-pawn bonuses. Talks to the env at `$MAKEFUN_ENV_URL` (`/game`, `/move`) in UCI; `main.py` is a packed (lzma) form of the engine and reads, imports or runs no other file.

## Run it

```sh
python3 main.py
```

## What changed in round 2

The v3 engine adds three features the v1 engine lacked, aimed at
pushing playing strength toward the sunfish baseline:

- **Null-move pruning** in search: when the side to move holds a queen
  or a bishop, is not in check, and the remaining depth is at least 3,
  the search first tries passing the turn. If even doing nothing keeps
  the score above beta, the branch is cut. This prunes hopeless lines
  much earlier than plain alpha-beta.
- **Passed-pawn bonus** in evaluation: a pawn with no opposing pawn on
  its own file or an adjacent file ahead of it earns a bonus that grows
  with how far it has advanced, since such a pawn is a lasting asset
  that can only be stopped by a piece.
- **Rook on open file bonus** in evaluation: a rook standing on a file
  with no pawns of either colour earns a bonus, rewarding the rook's
  long-range activity where it is not blocked by its own structure.

## Testing

Every change above was checked against the engine's own move generator
and search before being packed:

- **PERFT** from the start position gives 20, 400 and 8902 nodes at
  depths 1, 2 and 3, and the Kiwipete position gives 48, 2039 and
  97862 — the standard reference counts, so move generation is intact.
- **Determinism**: the search picks the same best move on repeated runs
  from the start position and from Kiwipete, so the new pruning and
  evaluation terms do not introduce any randomness or ordering noise.
- The packed `main.py` stays within the 4 KB limit (4,032 bytes).

## What changed in round 5

The v5 engine was rewritten from scratch (blind, from the kit spec) and
then golfed down to fit the 4 KB cap, replacing the round-4 engine:

- **PVS + late-move reductions** in search, with a transposition table
  that adjusts scores for mate distance, so the engine searches deeper
  on the same 40,000-node budget (the budget was lowered from 60,000
  after measurement showed 40,000 reaches the same depth at ~2.2 s/move).
- **Check extensions** and **null-move pruning (R=3)** to keep tactical
  lines accurate, plus **MVV-LVA quiescence** and repetition detection
  across the search path and game history.
- **Tapered middlegame/endgame evaluation**: piece-square tables that
  blend between middlegame and endgame values, with passed-pawn bonuses.
  (SEE, futility pruning, killer/history ordering, bishop pair, and the
  pawn-structure / king-safety / rook-file terms were cut to fit 4 KB.)

## Testing

Every change above was checked against the engine's own move generator
and search before being packed:

- **PERFT** from the start position gives 20, 400, 8902 and 197281
  nodes at depths 1–4, and the Kiwipete position gives 48, 2039 and
  97862 — the standard reference counts, so move generation is intact.
- **Determinism**: the search picks the same best move with identical
  node counts on repeated runs from the start position and from
  Kiwipete, so the new pruning and evaluation terms do not introduce
  any randomness or ordering noise.
- The packed `main.py` stays within the 4 KB limit (4,000 bytes).

---

<sub>Entered on [make.fun](https://make.fun/?ref=5hwq4sqk&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
