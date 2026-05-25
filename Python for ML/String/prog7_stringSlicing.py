# Slicing let us access part of string
# Syntax :- string[start :end]  ; end is excluded 

name ='Ayaan'
print(name[0:5])
print(name[0:4])
print(name[0:])
print(name[:3])
print(name[5:]) #nothing prints
print(name[-5:-1])
print(name[-5:0]) # nothing print beacuse negative indexes 0 should not be included 
print(name[-5:5])
print(name[-5:2])