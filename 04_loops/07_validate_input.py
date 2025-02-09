# Keep asking the user for a number until they enter a number between 1 and 10.

while True:
    input_num = int(input("Enter a number between 1 and 10: "))
    if input_num >= 1 and input_num <= 10:
        print(f"Thank you for entering {input_num}.")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 10.")

