from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            B=Bracket(next,i)
            opening_brackets_stack.append(B)
            

        if next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack and are_matching(opening_brackets_stack[-1].char,next):
                opening_brackets_stack.pop()
            else:
                return i
            
    # Can I add code here?
    if len(opening_brackets_stack)>0:
            return opening_brackets_stack[0].position



def main():
    i=input()
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch==None:
        print("Success")
    else:
        print(mismatch+1)


if __name__ == "__main__":
    main()
