##sum=n(n+1)/2
def sum(num):
    if num==1:
        return 1
    elif num<=0:
        return 0   
    else:
        return num+sum(num-1)

num=int(input("Enter a number: "))
a=sum(num)
print(a)