"""Two-Sentence Horror — entry for u-suroto-two-sentence-horror-acea9253.

Writes one original two-sentence horror story to /output/entry.txt.
The story is a fixed, hand-written text: no network, no randomness,
no input files. The grader only needs the file to exist and be valid
UTF-8 text of 1-400 characters.
"""

import os

STORY = (
    "I record my sleep to prove to my doctor that I talk in my sleep. "
    "Last night's recording is forty minutes of me, perfectly silent, "
    "listening to someone else talk in my voice."
)


def main() -> None:
    # Fail loudly instead of silently shipping an invalid entry:
    # the gate requires 1-400 characters and exactly two sentences.
    assert 1 <= len(STORY) <= 400, "story must be 1-400 characters"
    assert STORY.count(".") == 2, "story must be exactly two sentences"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
