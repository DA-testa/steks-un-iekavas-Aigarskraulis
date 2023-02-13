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
            # Process opening bracket, write your code here
             opening_brackets_stack.append(Bracket(next,i +1))
            if next in ")]}":
                
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1]/char,next):
                     return i+1
                    opening_brackets_stack.pop
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    reult =  find_mismatch(text)
    print(result)



if __name__ == "__main__":
    main()
