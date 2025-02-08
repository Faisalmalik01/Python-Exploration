# Suggest a pet food based on the pet type. The suggestions are as follows:
# - Dog: Dry food
# - Cat: Wet food
# - Bird: Seeds
# - Fish: Fish food
# - Rabbit: Hay
# - Other: Unknown

pet_type = input("Enter the type of pet (dog, cat, bird, fish, rabbit, other): ").lower()

if pet_type == "dog":
    pet_food = "Dry food"
elif pet_type == "cat":
    pet_food = "Wet food"
elif pet_type == "bird":
    pet_food = "Seeds"
elif pet_type == "fish":
    pet_food = "Fish food"
elif pet_type == "rabbit":
    pet_food = "Hay"
else:
    pet_food = "Unknown"

if pet_food != "Unknown":
    print(f"A {pet_type} should eat {pet_food}.")
else:
    print(f"Unknown pet type: {pet_type}.")

    