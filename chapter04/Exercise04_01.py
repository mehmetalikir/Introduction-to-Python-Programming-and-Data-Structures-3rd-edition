# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: area of a pentagon) Write a program that prompts the user to enter
the length from the center of a pentagon to a vertex and computes the area of the
pentagon, as shown in the following figure.'''

import math # Import math module to use the math functions

# Prompt the user to enter the length from the center of a pentagon to a vertex
r = float(input("Please enter the length from the center to vertex: "))

# Compute the area of the pentagon
s = (2 * r) * math.sin(math.pi / 5) # Length of a side
area = (5 * math.pow(s, 2)) / (4 * math.tan(math.pi / 5))

# Display result
print("The area of the pentagon is", format(area, "0.2f"))