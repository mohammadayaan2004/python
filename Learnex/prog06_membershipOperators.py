# Membership operators are used to check whether a value (element) exists
# inside a sequence (like string, list, tuple, set, dictionary).
def switch_Case(a, b, c):
    match c:
        case 1:
            print("IN Operator :-", a in b)
            # Returns True if the value is present in the sequence
        case 2:
            print("NOT IN Operator :-", a not in b)
            # Returns True if the value is not present in the sequence
        case _:
            print("Invalid Choice")
a = int(input("Enter num1 :- "))
#b = list(input("Enter num2 :- "))
# When you use input() in Python, it always gives you a string (text).
#So if you type 1 2 3 4 5, Python sees it as "1 2 3 4 5" — not numbers.
#To make them actual numbers, you must split the text and convert each piece to int.

b = list(map(int, input("Enter num2 :- ").split()))
c = int(input("Enter num from 1-2 based on operation that is required "))
switch_Case(a, b, c)