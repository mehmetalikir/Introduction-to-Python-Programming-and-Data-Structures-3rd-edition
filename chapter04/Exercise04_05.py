# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: area of a regular polygon) A regular polygon is an n-sided polygon in
which all sides are of the same length and all angles have the same degree (i.e., the
polygon is both equilateral and equiangular). The formula for computing the area
of a regular polygon is

area = n x s^2 / 4 x tan(pi / n)

Here, s is the length of a side. Write a program that prompts the user to enter the
number of sides and their length of a regular polygon and displays its area.'''

import math

# Prompt the user to enter the number of sides and their length of a regular polygon
sides = float(input("Please enter the number of sides: "))
s = float(input("Please enter the length of a side: "))

# Compute the area of the polygon
area = (sides * math.pow(s, 2) / (4 * math.tan(math.pi / sides)))

# Display its area
print(f"The are of the polygon is {area}")
