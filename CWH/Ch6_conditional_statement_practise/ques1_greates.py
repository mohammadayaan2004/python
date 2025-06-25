'''
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
num3=int(input("Enter num3 : "))
num4=int(input("Enter num4 : "))

if(num1>num4):
    f1=num1
else:
    f1=num4

if num2>num3:
    f2=num2
else:
    f2=num3

if f1>f2:
    print(str(f1)+" is greatest")
else:
    print(str(f2)+" is greatest")'''

numbers=[]
digit=int(input("Enter no of digits:- "))
print("Digits are :-")
for i in range (1,digit):
    num=int(input(f"Enter no {i} :-"))
    numbers.append(num)
    

great=max(numbers)
print(great)      