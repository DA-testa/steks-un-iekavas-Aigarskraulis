# python3
#Aigars,Kraulis,221RDC045,18.gr
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()

    if not opening_brackets_stack:
        return "Success"
    else:
        return opening_brackets_stack[-1].position


def main():
    choice = input()
    text = input()
    mismatch = find_mismatch(text)
    choice.upper()
    # Printing answer, write your code here
    if choice == "I":
        print(mismatch)
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
