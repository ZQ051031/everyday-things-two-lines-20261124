"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes the two-line entry to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = (
    "A toaster is like a tiny sun trapped in a metal box, giving your bread a quick suntan until it pops up golden-brown.\n"
    "The sun maps the heat and the browning, but leaves out that a toaster has no sunshine of its own — it only borrows electricity to glow red-hot."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
