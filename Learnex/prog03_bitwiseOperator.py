def switch_Case(a, b, c):
    match c:
        case 1:
            print("Bitwise AND :-", a & b)
            #  A  |  B  |  A & B
            #  0  |  0  |   0
            #  0  |  1  |   0
            #  1  |  0  |   0
            #  1  |  1  |   1

        case 2:
            print("Bitwise OR :-", a | b)
            #  A  |  B  |  A | B
            #  0  |  0  |   0
            #  0  |  1  |   1
            #  1  |  0  |   1
            #  1  |  1  |   1

        case 3:
            print("Bitwise NOT :-", ~a)
            #  A  |  ~A
            #  0  |  1
            #  1  |  0
            # (Note: In Python, ~A = -(A+1), 
            # because it uses 2's complement)

        case 4:
            print("Bitwise XOR :-", a ^ b)
            #  A  |  B  |  A ^ B
            #  0  |  0  |   0
            #  0  |  1  |   1
            #  1  |  0  |   1
            #  1  |  1  |   0

        case 5:
            print("Bitwise LEFT SHIFT :-", a << b)
            # Formula: a * (2^b)

        case 6:
            print("Bitwise RIGHT SHIFT :-", a >> b)
            # Formula: a // (2^b) (floor division)

        case _:
            print("Invalid Choice")


# Input
a = int(input("Enter num1 :- "))
b = int(input("Enter num2 :- "))
c = int(input("Enter num from 1-6 based on operation that is required "))
switch_Case(a, b, c)
