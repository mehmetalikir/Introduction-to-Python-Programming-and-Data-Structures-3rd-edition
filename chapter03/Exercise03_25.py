# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: intersecting point) Two points on line 1 are given as (x1, y1) and (x2,
y2) and on line 2 as (x3, y3) and (x4, y4), as shown in Figure 3.9a and Figure 3.9b.
The intersecting point of the two lines can be found by solving the following
linear equation:
				(y1 - y2)x - (x1 - x2)y = (y1 - y2)x1 - (x1 - x2)y1
				(y3 - y4)x - (x3 - x4)y = (y3 - y4)x3 - (x3 - x4)y3
This linear equation can be solved using Cramer’s rule (see Programming Exercise
3.3). If the equation has no solutions, the two lines are parallel(Figure 3.9c)
Write a program that prompts the user to enter four points and displays
the intersecting point.'''

# Prompt the user for inputs
x1 = float(input("Please enter x1: "))
y1 = float(input("Please enter y1: "))
x2 = float(input("Please enter x2: "))
y2 = float(input("Please enter y2: "))
x3 = float(input("Please enter x3: "))
y3 = float(input("Please enter y3: "))
x4 = float(input("Please enter x4: "))
y4 = float(input("Please enter y4: "))

# Calculate the intersecting point
a = y1 - y2
b = -1 * (x1 - x2)
c = y3 - y4
d = -1 * (x3 - x4)
e = (y1 - y2) * x1 - (x1 - x2) * y1
f = (y3 - y4) * x3 - (x3 - x4) * y3

# Solve the linear equation and display result
if (a * d - b * c) == 0:
    print("The equation has no solution.")
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("The intersecting point is at (", x, " and ", y, ")")
