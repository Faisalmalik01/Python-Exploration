# Create a functiom that returns both the area and circumference of a circle when the radius is given.

import math

def circle(radius): 
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return round(area), round(circumference)

radius = int(input("Enter radius: "))
area, circumference = circle(radius)
print(f"Area: {area}" , f"Circumference: {circumference}")


