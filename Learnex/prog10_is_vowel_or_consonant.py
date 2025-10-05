# Take a character from the user and check if it is a vowel or consonant.
ch=input("Enter a single alphabet letter: ")
vowels = 'aeiouAEIOU'
if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet letter only.")
else:
    if ch in vowels:
        print(f"{ch} is a vowel.")
    else:
        print(f"{ch} is a consonant.")
