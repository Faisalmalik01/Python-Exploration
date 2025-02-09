# Givena string, find the first non-repeated character in it.
# For example, the first non-repeated character in "total" is 'o' and the first non-repeated character in "teeter" is 'r'.

string = input("Enter a string: ")

for char in string:
    print(f"Checking {char}")
    if string.count(char) == 1:
        print(f"The first non-repeated character is {char}")
        break # we found the first non-repeated character, so we can stop the loop.




