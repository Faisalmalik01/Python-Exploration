#Electricity charges per unit:
#Up to 100 units → ₹5 per unit
#101 to 300 units → ₹8 per unit
#Above 300 units → ₹10 per unit
#Write a program that calculates the electricity bill based on the units consumed.

units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 8)
else:
    bill = (100 * 5) + (200 * 8) + ((units - 300) * 10)

print(f"Your electricity bill is ₹{bill}.")
