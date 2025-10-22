a=int(input("Enter num 1 :- "))
b=int(input("Enter num 2 :- "))
c=int(input("Enter num 3 :- "))
d=int(input("Enter num 4 :- "))
#if a>b and a>c and a>d:
#    print(a,"is greatest")
#elif b>c and b>a and b>d:
#    print(b,"is greatest")
#elif c>a and c>b and c>d:
#    print(c,"is greatest")
#elif d>a and d>b and d>c:
#    print(d,"is greatest")
#elif a==b==c==d:    
#    print("all number are equal")
#else :
#    print("Invalid Input")
greater=max(a,b,c,d)
print(greater,"is greatest")