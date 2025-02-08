# Choose a mode of transportation based on the distance to be travelled. The modes of transportation are as follows:
# - Short distance <3km: Walk
# - Medium distance 3-15km: Bike
# - Long distance >15km: Drive

distance = input("Enter the distance to be travelled in km: ")
distance_in_float = float(distance)

if distance_in_float < 3:
    transportation_mode = "Walk"
elif distance_in_float >= 3 and distance_in_float <= 15:
    transportation_mode = "Bike"
else:
    transportation_mode = "Drive"

print(f"Since the distance is {distance_in_float} km, you should {transportation_mode}.")
