"""
num=int(input("Enter a number: "))
fac=1
if num>=0:
    for i in range(1,num+1):
        fac=fac*i
    print(fac) 
else:
    print("Factorial not possible")     

    

def factorial(num):
    if num==0 or num ==1:
        return 1
    else:
        return num*factorial(num-1)  

num=int(input("Enter a number: "))    
a=factorial(num)
print("Factorial of the ",num, "is ", a)
"""
import math
num=int(input("Enter a number: "))
fac=math.factorial(num)
print(fac)
