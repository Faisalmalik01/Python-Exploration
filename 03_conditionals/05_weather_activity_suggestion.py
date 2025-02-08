# Suggest an activity based on the weather. The suggestions are as follows:
# - Sunny: Go for a walk
# - Cloudy: Watch a movie
# - Rainy: Read a book
# - Snowy: Drink hot chocolate

weather = input("Enter the weather (sunny, cloudy, rainy, snowy): ").lower()

if weather == "sunny":
    activity = "Go for a walk"
elif weather == "cloudy":
    activity = "Watch a movie"
elif weather == "rainy":
    activity = "Read a book"
elif weather == "snowy":
    activity = "Drink hot chocolate"
else:
    print("Invalid weather input. Please enter sunny, cloudy, rainy, or snowy.")

if weather in ["sunny", "cloudy", "rainy", "snowy"]:
    print(f"Since it's {weather}, you should {activity}.")