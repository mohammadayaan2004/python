##(0°C × 9/5) + 32 = 32°F
def far(cel):
    return ((cel * (9/5))+32)

    
temp=int(input("Enter temp in Celsius : "))
t=far(temp)
print("Celsius to Fahrenheit is : ",t)
