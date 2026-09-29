"""
scorer.py: decides whether one answer counts as correct.

run_eval.py imports `judge` from here. Whatever it returns is what shows up in
the Run columns:  True -> "pass", False -> "fail", None -> "—".

(The old version ended in `...`, so judge() returned None every time. That is
why every run printed "—".)

How `expects` works (set in questions.py):
  - One phrase:            "20 to 25 minutes"
  - Several allowed:       "second week|week two"   <- any one of them passes
  - The special word:      "REFUSE"                 <- the right behaviour is
                                                       to say "I don't know"
Matching ignores upper/lower case and extra spaces.
"""

import re

import gate

# Phrases the model uses when it says it can't answer. The gate's own refusal
# is one of them; the model's wording varies ("I do not have enough...").
REFUSAL_MARKERS = [
    gate.REFUSAL.lower(),
    "enough information",
    "no mention",
    "not mentioned",
    "no information",
]


def _normalise(text: str) -> str:
    """Lowercase, and squash runs of whitespace down to one space."""
    return re.sub(r"\s+", " ", (text or "").lower()).strip()


def is_refusal(answer: str) -> bool:
    text = _normalise(answer)
    return any(marker in text for marker in REFUSAL_MARKERS)


def judge(question, expects, answer, results) -> bool:
    """True if the answer is correct for this question."""
    expects = (expects or "").strip()

    # A question the corpus can't answer: saying "I don't know" is correct.
    if expects.upper() == "REFUSE":
        return is_refusal(answer)

    # Otherwise a refusal is always wrong.
    if answer == gate.REFUSAL:
        return False

    # Pass if ANY of the allowed phrases appears in the answer.
    text = _normalise(answer)
    options = [_normalise(o) for o in expects.split("|") if o.strip()]
    return any(option in text for option in options)


if __name__ == "__main__":
    # Quick self-test:  python scorer.py   -> should print True False True False
    print(judge("q", "second week|week two", "You can add through the end of the second week.", []))
    print(judge("q", "second week", "I don't have enough information about that.", []))
    print(judge("q", "REFUSE", "I do not have enough information to answer.", []))
    print(judge("q", "REFUSE", "CS offers a B.S. and a B.A.", []))
