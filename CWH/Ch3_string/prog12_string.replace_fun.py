name="please enjoy these great stories,(enjoy) fairy-tales, fables, and nursery rhymes for children. great"
print(name)

print("string.replace() function")
print('''This string will replace old words to new words''')
print('''This function will replace all the word present in a string''')
print(name.replace("please","aaaaa"))
print(name.replace("great","dfsvgubh"))

a = "Hello Anita I am in London and How are you?"
for i in a:
  print(i.replace('a','e'), end = '' )

#end='' is only needed when printing inside a loop to avoid newlines after each item; for a single 
#print() of a whole string, it’s not required.  