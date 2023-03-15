# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: points in triangle?) Suppose a right triangle is placed in a plane as
shown below. The right-angle point is placed at (0, 0), and the other two points
are placed at (200, 0), and (0, 100). Write a program that prompts the user to enter
a point with x- and y-coordinates and determines whether the point is inside the
triangle.'''

# Prompt the user for input
x = float(input("Please enter the x-coordinate of the point:"))
y = float(input("Please enter the y-coordinate of the point:"))

# Determine whether the point is inside the triangle
intersectionx = (-x * (200 * 100)) // (-y * 200 - x * 100)
intersectiony = (-y * (200 * 100)) // (-y * 200 - x * 100)
isIn = x < intersectionx or y < intersectiony

# Display result
if isIn:
    print("The point is in the triangle")
else:
    print("The point is not in the triangle")