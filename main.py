"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about a small everyday annoyance to
/output/entry.txt. Deterministic: the same text every run.
"""

import os

RANT = (
    "My neighbour starts his leaf blower at 7 a.m. on a Saturday. There "
    "are no leaves. The leaves left in October. He's just moving dust "
    "from one side of the driveway to the other, like a man who believes "
    "the noise is the work. He waves when he sees me. He waves."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT + "\n")


if __name__ == "__main__":
    main()
