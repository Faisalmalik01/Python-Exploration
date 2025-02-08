# Determine if a year is a leap year.
# A leap year is divisible by 4, but not by 100, unless it is divisible by 400.

year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

    