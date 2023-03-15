# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: point in a circle?) Write a program that prompts the user to enter a
point (x, y) and checks whether the point is within the circle centered at (0, 0)
with radius 10. For example, (4, 5) is inside the circle and (9, 9) is outside the
circle, as shown in Figure 3.8a.'''

import math

# Prompt the user to enter a point
x = float(input("Please enter the x-coordinate of the point: "))
y = float(input("Please enter the y-coordinate of the point: "))

# Check point is in the circle and display result
inCircle = math.pow((math.pow(x,2) + math.pow(y,2)), 0.5)
if inCircle <= 10:
    print("Point (",x, ", ", y,") is in the circle" )
else:
    print("Point (",x, ",", y,") is not in the circle" )


