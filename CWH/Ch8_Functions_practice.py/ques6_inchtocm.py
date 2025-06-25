# 1 inch = 2.54 cm
def unit(inch):
    cm=2.54*inch
    return cm

num=float(input("Enter number in inch: "))
a=unit(num)
print(a)  