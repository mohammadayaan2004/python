##  * * *    i=1    j=1,3,5   j>=1 or j==3 or j<=5
##  *   *    i=2    j=1, ,5   j
##  * * *    i=3    j=1,3,5

rows=3
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*",end=' ')
            
        else:
            print(" ",end=' ')
    print() 