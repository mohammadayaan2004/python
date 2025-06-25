# Print prime numbers less than 20
for num in range(2, 21):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if  prime==True:
        print(num)
