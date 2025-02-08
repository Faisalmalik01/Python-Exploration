# Customize a coffee order order: 
# - Small coffee is $2, medium is $3, and large is $4
# - An extra shot of espresso is $1
# - Print the total cost of the coffee order


size = input("What size coffee would you like? Small, Medium, or Large: ")
extra_shot = input("Would you like an extra shot of espresso? Yes or No: ")


if size.lower() == "small":
    price = 2
elif size.lower() == "medium":
    price = 3
else:
    price = 4

if extra_shot.lower() == "yes":
    price += 1

print(f"Your total is ${price}")

