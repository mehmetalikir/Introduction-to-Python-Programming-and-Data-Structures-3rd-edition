# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: point on the line segment) Programming Exercise 3.31 shows how to test
whether a point is on an unbounded line. Revise Programming Exercise 3.31 to
test whether a point is on a line segment. Write a program that prompts the user
to enter the three points for p0, p1, and p2 and displays whether p2 is on the line
segment from p0 to p1.'''

# Prompt the user to enter the three points for p0, p1, and p2
x0 = float(input("Please enter the x-coordinate of Point 0: "))
y0 = float(input("Please enter the y-coordinate of Point 0: "))
x1 = float(input("Please enter the x-coordinate of Point 1: "))
y1 = float(input("Please enter the y-coordinate of Point 1: "))
x2 = float(input("Please enter the x-coordinate of Point 2: "))
y2 = float(input("Please enter the y-coordinate of Point 2: "))

# Calculate point in on the line segment
str = ""
if (((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)) > 0 or
        ((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)) < 0 or
        (x2 < x0) or (y2 < y0) or (x2 > x1) or (y2 > y1)):
    str = "not"

# Display result
print("(", x2, ", ", y2, ") is", str, "on the line segment from (", x0, ", ", y0, ") to (", x1, ", ", y1, ")")
