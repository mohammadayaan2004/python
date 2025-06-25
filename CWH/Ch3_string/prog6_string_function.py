name="please enjoy these great stories,(enjoy) fairy-tales, fables, and nursery rhymes for children"
print(name)

print("len() function:-")
print("len() function which is use to find the number of character in the string ")
print(len(name))

print("string.endswith("") fun")
print('''It gives the ending of string
If it is ending with the gives function , it return True
else it return false''')
print(name.endswith("children"))#-->string.endswith fun -->TRUE
print(name.endswith("fvsgdhbj"))#-->string.endswith fun -->FALSE

print("string.count() function")
print(name.count("a"))
print(name.count("enjoy"))

print("string.capitalise() function") 
print("first letter of string is capital now")
print(name.capitalize())

print("string.find() function")
print('''It is find a character or group of charcters in a given sequence''')
print("It will only returns the first index of the character or group of charcters")
print(name.find("great"))
print(name.find("enjoy"))
print(name.find("Great"))

print("string.replace() function")
print('''This string will replace old words to new words''')
print('''This function will replace all the word present in a string''')
print(name.replace("please","aaaaa"))


