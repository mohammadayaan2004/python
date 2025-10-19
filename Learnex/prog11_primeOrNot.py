# Write a program that checks whether a given number is prime or not 
# (use if else).

num = int(input("Enter a number: "))
if num <= 1: 
    print(f"{num} is not a prime number")
else:
    for i in range (2,num):
        if ( num % i == 0):
            print(f"{num} is not a prime number")
            exit()
    
print(f"{num} is a prime number")

# Worst Case --->>> Number is prime → loop runs from 2 to num-1	--->>> O(n)
# Best Case --->>> Number divisible by 2 → stops early	--->>> O(1)
# Average Case --->>> Divisor found somewhere in between	--->>> O(n) approx.
# Space Complexity --->>> Only using a few variables	--->>> O(1) (Constant space)