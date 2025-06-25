num=int(input("Enter a number: "))
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break

if prime==True:
    print(str(num) +" "+ "is a prime number")
else:    
    print(str(num) +" "+ "is not a prime number")
