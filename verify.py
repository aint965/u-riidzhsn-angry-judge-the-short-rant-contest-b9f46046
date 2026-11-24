"""Verifier for the Angry Judge rant entry.

Runs main.py twice, checks determinism by comparing the sha256 of the
two outputs, then checks the gate: /output/entry.txt must be UTF-8 text
of 1 to 400 characters, not only whitespace.
"""

import hashlib
import subprocess
import sys

OUTPUT = "/output/entry.txt"


def run_main() -> None:
    result = subprocess.run(
        [sys.executable, "main.py"], check=True, capture_output=True, text=True
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)


def sha256_of(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        digest.update(f.read())
    return digest.hexdigest()


def main() -> int:
    run_main()
    first = sha256_of(OUTPUT)
    run_main()
    second = sha256_of(OUTPUT)

    print(f"run 1 sha256: {first}")
    print(f"run 2 sha256: {second}")
    deterministic = first == second
    print(f"deterministic: {'PASS' if deterministic else 'FAIL'}")

    try:
        with open(OUTPUT, "r", encoding="utf-8") as f:
            text = f.read()
    except UnicodeDecodeError:
        print("gate UTF-8: FAIL (not valid UTF-8)")
        return 1

    length = len(text)
    print(f"characters: {length}")
    print(f"gate 1-400 chars: {'PASS' if 1 <= length <= 400 else 'FAIL'}")
    print(f"gate not only whitespace: {'PASS' if text.strip() else 'FAIL'}")

    ok = deterministic and 1 <= length <= 400 and bool(text.strip())
    print(f"OVERALL: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
