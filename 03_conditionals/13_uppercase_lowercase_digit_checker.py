char = input("Enter a character: ")

if char.isdigit():
    print("The character is a digit.")
elif char.islower():
    print("The character is lowercase.")
elif char.isupper():
    print("The character is uppercase.")
else:
    print("Invalid input.")
