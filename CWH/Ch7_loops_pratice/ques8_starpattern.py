##      *          i=1   j=1       j<=1
##      **         i=2   j=1,2     j<=2
##      ***        i=3   j=1,2,3   j<=3

for i in range(1,4):
    for j in range(1,4):
        if j<=i:
            print("*",end='')
        else:
            print(" ",end='')
    print()            
