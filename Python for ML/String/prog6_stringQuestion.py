""" Question 
Write a Python program that takes a user’s name as input and prints:
The first character
The last character
The total length of the name
"""
name = input("Enter your name: ")
length = len(name)
first_character = name[0]
last_character = name[length - 1]
print("Total length:", length)
print("First character:", first_character)
print("Last character:", last_character)
