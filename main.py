"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about a small everyday annoyance to
/output/entry.txt. Deterministic: the same text every run.
"""

import os

RANT = (
    "My smoke detector chirps once at 3:12 a.m. One beep, then silence, "
    "just long enough for me to lie awake deciding whether my house is "
    "on fire or just haunted. I've changed the battery twice. It's a "
    "taunt \u2014 from nine feet up, where it knows I own no ladder."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT + "\n")


if __name__ == "__main__":
    main()
