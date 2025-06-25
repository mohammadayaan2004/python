'''# multiplication table using for loop
num1=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num1}x{i}={num1*i}")

## multiplication table using while loop'''
num=int(input("Enter a number: "))
j=1
while j<11:
    print(f"{num}x{j}={num*j}")
    j=j+1    