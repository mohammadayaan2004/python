##(0°C × 9/5) + 32 = 32°F
def cel(far):
    return ((far-32)*5/9)

    
temp=int(input("Enter temp in frahient : "))
t=cel(temp)
print("Frahient to Celius is : ",t)