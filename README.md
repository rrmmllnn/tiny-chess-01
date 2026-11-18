# tiny-chess-01 entry

Original 0x88 alpha-beta chess engine in 4 KB of Python (stdlib only).

- Fixed 50,000-node budget per move (iterative deepening, deterministic;
  no clock, no randomness), alpha-beta with transposition table,
  null-move and futility pruning, quiescence over captures/promotions
  and check evasions, material + piece-square evaluation, bishop pair.
- Talks to the env at `$MAKEFUN_ENV_URL` (`/game`, `/move`) in UCI.
- `main.py` is a packed (lzma) form of the engine; it reads, imports
  or runs no other file.

Build: `python3 dev/pack.py` regenerates `entry/main.py` from
`dev/engine.py` (development source, not part of the entry).
