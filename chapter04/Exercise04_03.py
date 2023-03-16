# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geography: estimate areas) Use the GPS locations for Atlanta, Georgia;
Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina in the figure
in Section 4.1 to compute the estimated area enclosed by these four cities.
(Hint: Use the formula in Programming Exercise 4.2 to compute the distance
between two cities. Divide the polygon into two triangles and use the formula in
Programming Exercise 2.14 to compute the area of a triangle'''

import math  # Import math module to use the math functions

RADIUS = 6371.01  # Constant value

# Let Atlanta, Orlando, and Savannah be the endpoints of the first triangle
# Let Atlanta, Charlotte, and Savannah be the endpoints of the second triangle
# Atlanta x1,y1-Orlando x2,y2 -Savannah x3,y3 - Charlotte x4,y4
x1 = -84.3879824
y1 = 33.7489954

x2 = -81.3792364999
y2 = 28.5383355

x3 = -81.09983419999998
y3 = 32.0835407

x4 = -80.84312669999997
y4 = 35.2270869

# Convert degrees to radians
x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)
x3 = math.radians(x3)
y3 = math.radians(y3)
x4 = math.radians(x4)
y4 = math.radians(y4)

# Calculate the  distances
# There is no need to calculate the distance from Atlanta to Savannah, because it is the side that bisects the triangle itself.
ab = RADIUS * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
ac = RADIUS * math.acos(math.sin(x1) * math.sin(x3) + math.cos(x1) * math.cos(x3) * math.cos(y1 - y3))
bc = RADIUS * math.acos(math.sin(x2) * math.sin(x3) + math.cos(x2) * math.cos(x3) * math.cos(y2 - y3))
ad = RADIUS * math.acos(math.sin(x1) * math.sin(x4) + math.cos(x1) * math.cos(x4) * math.cos(y1 - y4))
cd = RADIUS * math.acos(math.sin(x3) * math.sin(x4) + math.cos(x3) * math.cos(x4) * math.cos(y3 - y4))

# Calculate the area of triangles
s1 = (ab + ac + bc) / 2
s2 = (ad + cd + ac) / 2
area1 = math.pow(s1 * (s1 - ab) * (s1 - ac) * (s1 - bc), 0.5)
area2 = math.pow(s2 * (s2 - ad) * (s2 - ac) * (s2 - cd), 0.5)

# Calculate total area and display result
print("Total area of 4 points whose coordinates are given : ", (area1 + area2), " km^2.")

