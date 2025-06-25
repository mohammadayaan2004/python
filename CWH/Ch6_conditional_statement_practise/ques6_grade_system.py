mark=int(input("Enter your marks\n"))

if (mark>90):
    print("Your Grade is :Ex")
elif (mark<=90 and mark>80):
    print("Your Grade is :A")
elif (mark<=80 and mark>70):
    print("Your Grade is :B")
elif (mark<=70 and mark>60):
    print("Your Grade is :C")
elif (mark<=60 and mark>50):
    print("Your Grade is :D")    
else:
    print("Your Grade is :F")        