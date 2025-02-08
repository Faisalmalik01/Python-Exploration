# Assign a letter grade to a student based on their score. The grading scale is as follows:
# A: 90-100 B: 80-89 C: 70-79 D: 60-69 F: below 60

score = input("Enter your score: ")
score_in_int = int(score)

if score_in_int < 0 or score_in_int > 100:
    print("Invalid score")
    exit()

if score_in_int >= 90:
    print("You got an A")
elif score_in_int >= 80:
    print("You got a B")
elif score_in_int >= 70:
    print("You got a C")
elif score_in_int >= 60:
    print("You got a D")
else:
    print("You got an F")
