numbers=[]
digit=int(input("Enter number of digit :- "))

#range(start, stop) in Python includes the start 
#value but excludes the stop value.
#So if digit = 5, then range(1, 5) gives:
#[1, 2, 3, 4] — that’s only 4 numbers, not 5.

for i in range(1,digit+1):
    nums=int(input(f"Enter Number {i}:- "))
    numbers.append(nums)
greatest = max(numbers)
print(greatest) 