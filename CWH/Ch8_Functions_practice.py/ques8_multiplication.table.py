def multiTable(N,i):
    if i>10:
        return 
    print(f"{N}*{i}={N*i}")
    return multiTable(N,i+1)    



num=int(input("Enter a number: "))
print(f"Multiplication Table of {num} is : ")
multiTable(num,1)
