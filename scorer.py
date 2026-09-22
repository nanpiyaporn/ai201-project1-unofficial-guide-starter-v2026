import gate

def judge(question, expects, answer, results) -> bool:
    if answer == gate.REFUSAL:
        return False
    # your comparison here, using `expects`
    ...

if __name__ == "__main__":
    print(judge("test?", "late September", "Add/drop runs through late September.", []))
    print(judge("test?", "late September", "I don't have enough information about that.", []))
