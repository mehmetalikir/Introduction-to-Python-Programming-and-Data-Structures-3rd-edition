# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Corner point coordinates) Suppose a pentagon is centered at (0, 0) with one point
at the 0 o’clock position, as shown in Figure 4.11c. Write a program that prompts
the user to enter the radius of the bounding circle of a pentagon and displays the
coordinates of the five corner points on the pentagon.'''

import math

# Prompt the user to enter the radius of the bounding circle of a pentagon
radius = float(input("Please enter the radius of the bounding circle: "))


# displays the coordinates of the five corner points on the pentagon
x1 = radius * math.sin(2 * math.pi / 5)
y1 = radius * math.cos(2 * math.pi / 5)
print(x1 , " " , y1)
x2 = radius * math.sin(2 * math.pi / 5 * 2)
y2 = radius * math.cos(2 * math.pi / 5 * 2)
print(x2 , " " , y2)
x3 = radius * math.sin(2 * math.pi / 5 * 3)
y3 = radius * math.cos(2 * math.pi / 5 * 3)
print(x3 , " " , y3)
x4 = radius * math.sin(2 * math.pi / 5 * 4)
y4 = radius * math.cos(2 * math.pi / 5 * 4)
print(x4 , " " , y4)
x5 = radius * math.sin(2 * math.pi / 5 * 5)
y5 = radius * math.cos(2 * math.pi / 5 * 5)
print(x5  , " " , y5)
