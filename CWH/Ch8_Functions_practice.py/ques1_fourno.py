def maximum(num1,num2,num3,num4):
    if num1>num2:
        f1=num1
    else:
        f1=num2    
    if num3>num4:
        f2=num3
    else:
        f2=num4  
    if f1>f2:
        return f1
    else:
        return f2        

        
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
num3=int(input("Enter num3 : "))
num4=int(input("Enter num4 : "))

m=maximum(num1,num2,num3,num4)
print(m)