sub1=int(input("Enter marks of sub1 "))
sub2=int(input("Enter marks of sub2 "))
sub3=int(input("Enter marks of sub3 "))

total=(sub1+sub2+sub3)/3


if (total>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("You are pass")
else:
    print("You are fail")    