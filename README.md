# The Saturday Leaf Blower

[![Angry Judge: The Short Rant Contest](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/aint965/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/aint965/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

An entry for [Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) on make.fun.

## What the entry is

`main.py` (Python 3.13, no network, no secrets) writes one short, funny rant
about a small everyday annoyance — a neighbour's 7 a.m. Saturday leaf
blower, used on a driveway with no leaves — to `/output/entry.txt`. The program is fully deterministic: it writes
the same text on every run. `verify.py` runs `main.py` twice, compares the
sha256 of both outputs, and checks the gate (UTF-8 text, 1–400 characters,
not only whitespace).

## The rant

> My neighbour starts his leaf blower at 7 a.m. on a Saturday. There are no leaves. The leaves left in October. He's just moving dust from one side of the driveway to the other, like a man who believes the noise is the work. He waves when he sees me. He waves.

259 characters including the trailing newline.

## Run it

```sh
python3 main.py    # writes /output/entry.txt
python3 verify.py  # determinism + gate check, prints PASS/FAIL
```

## License

MIT — see [LICENSE](LICENSE).
