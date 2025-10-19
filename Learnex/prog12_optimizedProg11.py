# Write a program that checks whether a given number is prime or not 
# (use if else).
# Optimized version

def is_prime(num):
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

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Time Complexity: O(√n)
# Space Complexity: O(1) → constant space used
