##      *         i=1   j=    3       j>=3 and j<=3
##     ***        i=2   j=  2,3,4     j>=2 and j<=4
##    *****       i=3   j=1,2,3,4,5   j>=1 and j<=5
##                                    j>=4-i and j<=i+2
 
for i in range(1,4):
    for j in range(1,6):
        if j>=4-i and j<=i+2:
            print("*",end='')
        else:
            print(" ",end='')
    print()    