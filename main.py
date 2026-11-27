#!/usr/bin/env python3
"""Write one short thank-you text to /output/entry.txt.

No network, no input files, no randomness: the text is fixed.
"""
import os

TEXT = """Thank you for staying with this one a little longer.

You have read so many of these today, each one asking, in its own way, to be chosen. I will not ask for that. I only wanted to say that I noticed the quiet part of your work: the reading no one applauds, the care you give to words that will never know your name.

Somewhere, while you were reading, a kettle went quiet. A window cooled. The day moved on without you, and you stayed anyway, turning each page gently, as if it mattered.

It did. This one mattered, because you read it all the way through.

Thank you for the pause you gave it. I hope the light is still on in the next room when you finish, and someone is keeping a chair warm for you."""

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
