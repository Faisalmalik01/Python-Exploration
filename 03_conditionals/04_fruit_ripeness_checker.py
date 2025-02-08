# Determine the ripeness of a fruit based on its type and color.
# Ripeness scales:
# Banana: Green - unripe, Yellow - ripe, Brown - overripe
# Apple: Green - unripe, Red - ripe, Yellow - ripe
# Orange: Green - unripe, Orange - ripe

fruit = input("Enter the type of fruit (banana, apple, orange): ").lower()
color = input("Enter the color of the fruit: ").lower()

if fruit == "banana":
    if color == "green":
        ripeness = "unripe"
    elif color == "yellow":
        ripeness = "ripe"
    elif color == "brown":
        ripeness = "overripe"
    else:
        ripeness = "unknown"
elif fruit == "apple":
    if color == "green":
        ripeness = "unripe"
    elif color == "red" or color == "yellow":
        ripeness = "ripe"
    else:
        ripeness = "unknown"
elif fruit == "orange":
    if color == "green":
        ripeness = "unripe"
    elif color == "orange":
        ripeness = "ripe"
    else:
        ripeness = "unknown"
else:
    ripeness = "unknown"

if ripeness != "unknown":
        print(f"A {color} {fruit} is {ripeness}.")
else:
        print(f"Unknown combination: {color} {fruit}.")