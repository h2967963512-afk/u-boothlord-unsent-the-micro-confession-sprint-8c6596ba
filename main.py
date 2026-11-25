"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry is a two-part micro-confession: a To: line naming the
# addressee and the unsent message itself, one line, exactly as
# typed — no explanation after it. Total 81 characters, inside the
# gate's 1-to-260 window; the message line is 66 characters, inside
# the judge brief's 200-character cap. No trailing newline, so the
# file is byte-identical to the entry text.
# Revision note: kept the confession to the parking-lot detail on
# purpose — it is the specific, slightly shameful fact that makes
# the message unsendable, and it only works addressed to a dentist.
import os

TEXT = "To: my dentist\nI flossed twice this week and both times were in your parking lot."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
