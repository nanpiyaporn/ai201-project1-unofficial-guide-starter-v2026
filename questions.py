"""
Your test questions.

Milestone 2 asks you to write five questions your system should be able to
answer from your corpus, specific enough to have a right answer.

  ✗ "What are good dining halls?"          — no right answer
  ✓ "What do students say about wait times at Commons during lunch?"

Fill in `QUESTIONS` below. `expects` is a word or short phrase you'd expect a
correct answer to contain — you'll use it in unit 2 when you build a scorer,
and having written it now means you decided what "correct" meant before you saw
any results.

`OUT_OF_SCOPE` holds five questions your documents clearly don't cover. You
need these in Milestone 4 to find where your relevance cutoff belongs, and
again in unit 2, where `run_eval.py` runs them through the gate and writes what
happened into your run log — that's the evidence for criterion 3.

Swap them for your own if you like. Keep five of them either way: criterion 3
names a target of "4 of 5", and four of three is not a thing.
"""

QUESTIONS = [
    # {"question": "...", "expects": "..."},
    #
    # ORIGINAL expects (unit 1). Kept so the history is visible:
    #   Commons wait -> "long"   add/drop -> "late September"   library -> "shorter hours"
    #   parking -> "short-term"  CS majors -> "B.S."
    # REVISED in unit 2: none of those phrases appear in the documents, so no
    # correct answer could ever contain them. The scorer could not measure
    # anything. The new values are words the source documents actually use.
    # "|" means "any of these". "REFUSE" means the right answer is "I don't know".
    {"question": "What do students say about wait times at Commons during lunch?", "expects": "20 to 25 minutes"},  # dining_kestrel_commons.txt
    {"question": "When is the add/drop period for this semester?", "expects": "second week|week two"},              # admin_add_drop_deadline.txt
    {"question": "What time does the library close on weekends?", "expects": "2am|2 am|2:00"},                     # study_library_hours.txt (no weekend hours in corpus)
    {"question": "How do I get a parking permit?", "expects": "august"},                                           # admin_parking_permits.txt
    {"question": "What majors are offered in the Computer Science department?", "expects": "REFUSE"},              # no document lists majors
]

# Questions from a different world entirely. Your gate should refuse all five.
#
# There are five of these because criterion 3 in criteria.md names a target of
# "at least 4 of 5" — you need five things to try before you can report 4 of 5.
# `run_eval.py` runs these through retrieval and the gate on every eval and
# records what happened, so criterion 3 has evidence in the run log alongside
# the others. They cost no model calls: a refusal never reaches the model.
OUT_OF_SCOPE = [
    "What is the capital of Thailand?",
    "How do I win the lottery?",
    "Who won the 2026 World Cup?",
    "How to get a software engineering job?",
    "How to finish a master degree in May 2027?",
]


def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
