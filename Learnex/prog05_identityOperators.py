#Identity operators in Python are used to check if two objects (variables) 
# are stored at the same memory location.
def switch_Case(a, b, c):
    match c:
        case 1:
            print("IS Operator :-", a is b)
            # Returns True if both variables point to the same object
        case 2:
            print("IS NOT Operator :-", a is not b)
            # Returns True if both variables do not point to the same object
        case _:
            print("Invalid Choice")
a = int(input("Enter num1 :- "))
b = int(input("Enter num2 :- "))
c = int(input("Enter num from 1-2 based on operation that is required "))
switch_Case(a, b, c)
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y) # False because x and y are different objects in memory