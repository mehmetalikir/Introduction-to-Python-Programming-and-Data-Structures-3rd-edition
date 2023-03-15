# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: point in a rectangle?) Write a program that prompts the user to enter
a point (x, y) and checks whether the point is within the rectangle centered at
(0, 0) with width 10 and height 5. For example, (2, 2) is inside the rectangle and
(6, 4) is outside the rectangle, as shown in Figure 3.7b. (Hint: A point is in the
rectangle if its horizontal distance to (0, 0) is less than or equal to 10 / 2 and its
vertical distance to (0, 0) is less than or equal to 5.0 / 2. Test your program to
cover all cases.)'''

import math

# Prompt the user to enter a point
x = float(input("Please enter the x-coordinate of the point: "))
y = float(input("Please enter the y-coordinate of the point: "))

# Check point is in the rectangle and display result
horizontal = (math.pow(math.pow(x, 2), 0.5))
vertical = (math.pow(math.pow(y, 2), 0.5))
if horizontal <= 5.0 and vertical <= 2.5:
    print("Point (", x, ", ", y, ") is in the rectangle")
else:
    print("Point (", x, ",", y, ") is not in the rectangle")
