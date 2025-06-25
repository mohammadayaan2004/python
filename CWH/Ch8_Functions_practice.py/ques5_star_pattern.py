##  ***    i=1   j<=3
##  **     i=2   j<=2
##  *      i=3   j<=1    
##           j<=4-i

for i in range(1,4):
    for j in range(1,4):
        if j<=4-i:
            print("*",end='')
        else:
            print(" ",end='')
    print()            

