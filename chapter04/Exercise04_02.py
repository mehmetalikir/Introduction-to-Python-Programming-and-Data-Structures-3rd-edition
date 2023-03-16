# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: great circle distance) The great circle distance is the distance between
two points on the surface of a sphere. Let (x1, y1) and (x2, y2) be the geographical
latitude and longitude of two points. The great circle distance between the two
points can be computed using the following formula:

d = radius * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))

Write a program that prompts the user to enter the latitude and longitude of two
points on the earth in degrees and displays its great circle distance. The average
earth radius is 6,371.01 km. Note that you need to convert the degrees into radians
using the math.radians method since the Python trigonometric functions use
radians. The latitude and longitude degrees in the formula are for north and west.
Use negative to indicate south and east degrees.'''

import math  # Import math module to use the math functions

RADIUS = 6371.01  # Constant value

# Prompt the user to enter the latitude and longitude of two points on the earth in degrees
x1 = float(input("Please enter point1's latitude in degrees: "))
y1 = float(input("Please enter point1's longitude in degrees: "))
x2 = float(input("Please enter point2's latitude in degrees: "))
y2 = float(input("Please enter point2's longitude in degrees: "))

# Convert degrees to radians
x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

# Calculate its great circle distance
d = RADIUS * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

# Display its great circle distance
print("The distance between the two points in", d, "km")
