# Check if a password is is weak, medium or strong.
# - A password is weak if it is less than 6 characters long.
# - A password is medium if it is between 6 and 10 characters long.
# - A password is strong if it is more than 10 characters long.

password = input("Enter your password: ")
password_length = len(password)

if password_length < 6:
    strength = "weak"
elif password_length >= 6 and password_length <= 10:
    strength = "medium"
else:
    strength = "strong"

print(f"Your password is {strength}.")