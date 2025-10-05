def assignment_ops(choice,x,y):
    match choice:
        case 1:
            x = y
            print("= Operator ", x)
        case 2:
            x += y
            print("+= Operator ", x)
        case 3:
            x -= y
            print("-= Operator ", x)
        case 4:
            x *= y
            print("*= Operator ", x)
        case 5:
            x /= y
            print("/= Operator ", x)
        case 6:
            x %= y
            print("%= Operator ", x)
        case 7:
            x //= y
            print("//= Operator ", x)
        case 8:
            x **= y
            print("**= Operator ", x)
        case 9:
            x &= y
            print("&= Operator ", x)
        case 10:
            x |= y
            print("|= Operator ", x)
        case 11:
            x ^= y
            print("^= Operator ", x)
        case 12:
            x >>= y
            print(">>= Operator ", x)
        case 13:
            x <<= y
            print("<<= Operator ", x)
        case 14:
            print(n := x)  
        case _:
            print("Invalid choice!")

print("Assignment Operators Menu:")
print("1.=   2.+=   3.-=   4.*=   5./=   6.%=   7.//=   8.**=")
print("9.&=  10.|=  11.^=  12.>>=  13.<<=  14.:=")

ch = int(input("Enter your choice (1-14): "))
a = int(input("Enter num1 :- "))
b = int(input("Enter num2 :- "))
assignment_ops(ch,a,b)
