class Employee:
    Company="Google"  #class attributes
    salary=100

ayaan=Employee()  #object instantiation
ammar=Employee()

#creating instance attribute
ayaan.salary=123345

print(ayaan.salary)
print(ammar.salary)

#instance attribute take prefence over class attributes