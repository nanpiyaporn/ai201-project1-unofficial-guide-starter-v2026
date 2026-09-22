# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
 e.g. "One of my questions is about a topic only two documents mention, so
     I expect that one to be hard." 
  "question 1 ": "What do students say about wait times at Commons during lunch?", "expects 1 ": "long",
  The answer is Students say that wait times at Kestrel Commons are 20 to 25 minutes between 12:15 and 1:00. It check from the document more than the expectation:
  I give 80% reasonable based on document

"question 2": "When is the add/drop period for this semester?", "expects": "late September",
     You can add a course through the end of the second week, and dropping runs through the end of week six. (Source: admin_add_drop_deadline.txt)

Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_study_abroad.txt, admin_withdrawal_deadline.txt, course_cs_340.txt

The answer is rely on document more than expectation
I gave 80% reasonable based on document

"question 3": "What time does the library close on weekends?", "expects": "shorter hours",
The answer:Based on the provided documents, there is no mention of what time the library closes on weekends; it only states that the library is open until 2am during term and until 10pm during reading week. 

Source: `study_library_hours.txt`
There are not exactly answer on both document and the expectation.
I gave 85% reasonable because there are no exact time the use ask for. The system try to find the best answer that accepted. 

 "question 4": "How do I get a parking permit?", "expects": "short-term",
 Based on the provided documents, student permits for the west lots go on sale in August. The documents do not explain the exact purchasing process beyond stating when they go on sale. 

Source: `admin_parking_permits.txt`
I give 85% reasonable based on the document. Not rely on expectation

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
Why all five and not four? What about your setup makes that achievable —
     or what would have to go wrong for it not to be?

1. "question 1 ": "What do students say about wait times at Commons during lunch?" Source: `dining_kestrel_commons.txt`
2. "question 2":"When is the add/drop period for this semester?" (Source: admin_add_drop_deadline.txt)
3. "question 3": "What time does the library close on weekends?"
(Source: study_library_hours.txt )
4. question 4": "How do I get a parking permit?"
(Source: admin_parking_permits.txt )
---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. 

**Why this target:**
 What did your distances look like when you set the cutoff in Milestone 4?
     Was there a clean gap, or did the two groups overlap?

---

## 4. Something about your chunks

All my 5 chunks are ok. did not break any of these document into multiple pieces. It may 
see a multiple line. but the chunk size is getting longer and longer in each chunk. The chuck number 5 it longest one with 516 chars, it seem too long.


**Why this target:**



---

## 5. Your choice

I should read the txt file, and ask the right question. For example, when I ask what time is the library open on the 
weekend. It do not have the right answer.



**Why this target:**
Because the right answer come from the document, that why we need to know the content first. before asking the question.
After that we can compare if it return the right size of chuck.


---

The
─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
