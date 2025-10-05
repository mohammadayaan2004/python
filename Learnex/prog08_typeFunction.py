print(type(10))            # <class 'int'>
print(type(3.14))          # <class 'float'>
print(type("hello"))       # <class 'str'>
print(type([1, 2, 3]))     # <class 'list'>
print(type((1, 2)))        # <class 'tuple'>
print(type({"a": 1}))      # <class 'dict'>
print(type({1, 2}))        # <class 'set'>
print(type(True))          # <class 'bool'>
print(type(None))          # <class 'NoneType'>

def f(): 
    pass
print(type(f))             # <class 'function'>

class Dog: 
    pass
d = Dog()
print(type(d))             # <class '__main__.Dog'>
print(type(lambda x: x))   # <class 'function'>

enter = type(input("Enter something: "))
print("The type of the variable is:", enter)
#The input() function always returns a 
# string (no matter if you type 123, 3.14, or True).
#If you type 123, the type is still <class 'str'>.


