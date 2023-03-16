# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: area of a hexagon) The area of a hexagon can be computed using the
following formula (s is the length of a side):
area = 6 x s^2 / 4 x tan(pi/6)
Write a program that prompts the user to enter the side of a hexagon and displays
its area.'''

import math

# Prompt the user to enter the side of a hexagon
s = float(input("Please enter the side: "))

# Compute the area of a hexagon
area = (6 * math.pow(s, 2)) / (4 * math.tan(math.pi / 6))

# Display result
print(f"The are of the hexagon is {area}")
