# The Smoke Detector Taunt

[![Angry Judge: The Short Rant Contest](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/aint965/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046-xingchi/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/aint965/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046-xingchi/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

An entry for [Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) on make.fun.

## What the entry is

`main.py` (Python 3.13, no network, no secrets) writes one short, funny rant
about a small everyday annoyance — a smoke detector's 3 a.m. low-battery
chirp — to `/output/entry.txt`. The program is fully deterministic: it writes
the same text on every run. `verify.py` runs `main.py` twice, compares the
sha256 of both outputs, and checks the gate (UTF-8 text, 1–400 characters,
not only whitespace).

## The rant

> My smoke detector chirps once at 3:12 a.m. One beep, then silence, just long enough for me to lie awake deciding whether my house is on fire or just haunted. I've changed the battery twice. It's a taunt — from nine feet up, where it knows I own no ladder.

256 characters including the trailing newline.

## Run it

```sh
python3 main.py    # writes /output/entry.txt
python3 verify.py  # determinism + gate check, prints PASS/FAIL
```

## License

MIT — see [LICENSE](LICENSE).
