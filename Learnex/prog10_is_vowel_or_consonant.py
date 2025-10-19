# Take a character from the user and check if it is a vowel or consonant.
#ch=input("Enter a single alphabet letter: ")
#vowels = 'aeiouAEIOU'
#if len(ch) != 1 or not ch.isalpha():
#    print("Please enter a single alphabet letter only.")
#else:
#    if ch in vowels:
#        print(f"{ch} is a vowel.")
#    else:
#        print(f"{ch} is a consonant.")

# Take a string from the user and check if it has a vowel or consonant.
str=input("Enter a string: ")
vowels = 'aeiouAEIOU'
vowels_found = False
for char in str:
    if char in vowels:
        vowels_found = True
        break

if vowels_found:
    print("The string contains at least one vowel.")    
else:
    print("The string does not contain any vowels.")