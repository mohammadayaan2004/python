def primeNumber(num):
    if num <= 1: 
        return False
    elif num == 2:  
        return True 
    elif num%2==0:
        return False 
    else:
        i=3
        while i*i<=num:
            if ( num % i == 0):
                return False
        i += 2
    return True 
a=int(input("Enter the starting range: "))
b=int(input("Enter the ending range: "))
print("Prime Numbers betwen ", a , " and ",b, " are:- ")
for i in range(a,b):
    if primeNumber(i):
        print(i)

#Prime check of 1 number --->>> O(√n)
#Prime check in a range	--->>>O((b - a) × √n) main yeh wala hai
#Space Complexity --->>> O(1 )       