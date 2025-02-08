# Movie tickets are priced based on age : $12 for adults(18 and over), $8 for children(3-17), Everyone gets a $2 discount on Wednesday.

age = input("Enter your age: ")
age_in_int = int(age)

day = input("Enter the day of the week: ")
price = 0

if age_in_int >= 3 and age_in_int <= 17:
    price = 8
elif age_in_int >= 18:
    price = 12

if day == "wednesday":
    # price = price - 2
    price -= 2

print(f"Your ticket price is ${price}")



# age = input("Enter your age: ")
# age_in_int = int(age)
# day = input("Enter the day of the week: ")
# price = 12 if age >= 18 else 8
# if day = "wednesday":
#     price -= 2
# print(f"Your ticket price is ${price}")
