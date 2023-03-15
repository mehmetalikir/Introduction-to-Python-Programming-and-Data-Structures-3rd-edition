# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: two circles) Write a program that prompts the user to enter the center
coordinates and radius of two circles and determines whether the second circle is
inside the first or overlaps with the first, as shown in Figure 3.11.
(Hint: circle2 is inside circle1 if the distance between the two centers
6 = |r1 - r2| and circle2 overlaps circle1 if the distance between the two centers
<= r1 + r2. Test your program to cover all cases.)'''

import math

# Prompt the user to enter the center coordinates and radius of two circles
circle1X = float(input("Please enter circle1's center x-coordinate: "))
circle1Y = float(input("Please enter circle1's center y-coordinate: "))
circle1Radius = float(input("Please enter circle1's radius: "))
circle2X = float(input("Please enter circle2's center x-coordinate: "))
circle2Y = float(input("Please enter circle2's center y-coordinate: "))
circle2Radius = float(input("Please enter circle2's radius: "))

# Determine whether the second circle is inside the first or overlaps with the first
if (math.pow(math.pow(circle2X - circle1X, 2) + math.pow(circle2Y - circle1Y, 2), 0.5) <=
        math.fabs(circle1Radius - circle2Radius)):
    print("circle2 is inside circle1")
elif (math.pow(math.pow(circle2X - circle1X, 2) + math.pow(circle2Y - circle1Y, 2), 0.5) <=
      circle1Radius + circle2Radius):
    print("circle2 overlaps circle1")
else:
    print("circle2 does not overlap circle1")
