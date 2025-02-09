# Reverse a string using a loop.

string = input("Enter a string: ")

reversed_string = ""
for char in string:
    reversed_string = char + reversed_string  #it's prepending each character.

print(reversed_string)

