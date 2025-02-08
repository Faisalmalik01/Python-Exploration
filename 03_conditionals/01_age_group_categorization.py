# Classify a person's age group : child(0-12), teenager(13-19), adult(20-59), senior(60+)
age = input("Enter your age: ")
age_in_int = int(age)

if age_in_int >= 0 and age_in_int <= 12:
    print("You are a child")
elif age_in_int >= 13 and age_in_int <= 19:
    print("You are a teenager")
elif age_in_int >= 20 and age_in_int <= 59:
    print("You are an adult")
else:
    print("You are a senior")   

