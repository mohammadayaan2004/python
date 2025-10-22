def primeNumber(num):
   print("Prime Numbers betwen ", a , " and ",b, " are:- ")
for i in range(a,b):
    if primeNumber(i):
        print(i)
a=int(input("Enter the starting range: "))
b=int(input("Enter the ending range: "))
sieve_of_eratosthenes(a, b)


#Prime check in a range	--->>>O(n log log n)
#Space Complexity --->>> O(n)       