def switch_Case(a, b, c):
    match c:
        case 1:
            print("AND Operator :-", a>0 and b>0)
        case 2:
            print("OR Operator :-", a>0 or b>0)
        case 3:
            print("NOT Operator :-", not(a>0))
        case _:
            print("Invalid Choice")

a = int(input("Enter num1 :- "))
b = int(input("Enter num2 :- "))
c = int(input("Enter num from 1-3 based on operation that is required "))
switch_Case(a, b, c)