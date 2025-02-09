# Check if all elements in a list are unique. 
# if dubliactes are found, exit the loop and print duplicates found.

items = ["apple", "banana", "cherry", "apple", "mango"]

unique_items = set()

for item in items:
    if item in unique_items:
        print(f"Duplicate found: {item}")
        break
    unique_items.add(item)
