class Employee:
    Company="Google"  #class attributes

ayaan=Employee()  #object instantiation
print(ayaan.Company)
ammar=Employee()
print(ammar.Company)
'''
ayaan.Company="Yt"
ammar.Company="microsoft"
print(ayaan.Company)
print(ammar.Company)
'''

Employee.Company="Flipkart"  #changing class attributes
print(ayaan.Company)
print(ammar.Company)