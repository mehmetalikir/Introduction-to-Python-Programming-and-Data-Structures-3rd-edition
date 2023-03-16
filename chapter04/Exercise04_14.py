# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Random points on a circle) Write a program that generates three random points
on a circle centered at (0, 0) with radius 40 and display three angles in a triangle
formed by these three points, as shown in Figure 4.11a. (Hint: Generate a random
angle α in radians between 0 and 2π, as shown in Figure 4.11b and the point determined
by this angle is (r*cos(a), r*sin(a)).)'''

import math
import random

# Constant
RADIUS = 40

# Randomize the alpha angle in Figure b.
alpha1 = random.random() * 2 * math.pi
alpha2 = random.random() * 2 * math.pi
alpha3 = random.random() * 2 * math.pi
alpha4 = random.random() * 2 * math.pi
alpha5 = random.random() * 2 * math.pi
# alpha6 = (random.random() * (2 * math.pi))

#  alpha1 = random.random() * 1000 % 360
#  alpha2 = random.random() * 1000 % 360
#  alpha3 = random.random() * 1000 % 360
#  alpha4 = random.random() * 1000 % 360
#  alpha5 = random.random() * 1000 % 360
alpha6 = random.random() * 1000 % 360

# Assign the points x1,y1-x2,y2-x3-y as coordinates.
x1 = RADIUS * math.cos(alpha1)
y1 = RADIUS * math.sin(alpha2)
x2 = RADIUS * math.cos(alpha3)
y2 = RADIUS * math.sin(alpha4)
x3 = RADIUS * math.cos(alpha5)
y3 = RADIUS * math.sin(alpha6)

# Calculate the distance between two points
a = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
b = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
c = math.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))

# Find the inner angles of the triangle and convert radians to degrees.
A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

print("Interior of the triangle : ", "\nA :", (round(A * 100) / 100.0),
      " \nB :", (round(B * 100) / 100.0), " \nC :", (round(C * 100) / 100.0))

# *Constant
print("The sum of the interior angles of the triangle :", round(A + B + C))
