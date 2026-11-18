# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rrmmllnn/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rrmmllnn/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Original 0x88 alpha-beta chess engine in 4 KB of Python (stdlib only): fixed 50,000-node budget per move, deterministic, with transposition table, null-move and futility pruning, quiescence over captures/promotions and check evasions, material + piece-square evaluation, bishop pair. Talks to the env at `$MAKEFUN_ENV_URL` (`/game`, `/move`) in UCI; `main.py` is a packed (lzma) form of the engine and reads, imports or runs no other file.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=5hwq4sqk&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
