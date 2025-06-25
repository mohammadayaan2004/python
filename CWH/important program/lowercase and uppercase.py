name=input("Enter a string:-")
special=0
lower=0
upper=0
for i in name:
	if(i.islower()):
		lower+=1
	elif(i.isupper()):
		upper+=1
	else:
		special+=1
				
print("The number of lowercase characters is:",lower)
print("The number of uppercase characters is:",upper)
print("The number of uppercase characters is:",special)
