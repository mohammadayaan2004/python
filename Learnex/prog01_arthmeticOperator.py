def switch_Case(a,b,c):
    match c:
        case 1:
            print("Addition :- ", a + b)
        case 2:
            print("Subtraction :- ", a - b)
        case 3:
            print("Multiplication :- ", a * b)
        case 4:
            print("Division :- ", a / b if b != 0 else "Division by zero not allowed")
        case 5:
            print("Modulus :- ", a % b)
        case 6:
            print("Power :- ", a ** b)
        case _:
            print("Invalid Choice")
# /  → normal division → keeps decimal.
# // → floor division → removes decimal and rounds down towards negative infinity
a=int(input("Enter num1 :- "))
b=int(input("Enter num2 :- "))
c=int(input("Enter num from 1-6 based on operation that is required "))
switch_Case(a,b,c)
