# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: point position) Given a directed line from point p0(x0, y0) to p1(x1,
y1), you can use the following condition to decide whether a point p2(x2, y2) is
on the left of the line, on the right of the line, or on the same line(see Figure 3.12)'''

# Prompt the user to enter the three points for p0, p1, and p2
x0 = float(input("Please enter the x-coordinate of Point 0: "))
y0 = float(input("Please enter the y-coordinate of Point 0: "))
x1 = float(input("Please enter the x-coordinate of Point 1: "))
y1 = float(input("Please enter the y-coordinate of Point 1: "))
x2 = float(input("Please enter the x-coordinate of Point 2: "))
y2 = float(input("Please enter the y-coordinate of Point 2: "))

# Calculate point position
position = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

# Display result
str = ""
if position > 0:
    str = "left side of the"
if position < 0:
    str = "right side of the"

print("(", x2, ", ", y2, ") is on the", str, "line from (", x0, ", ", y0,
      ") to (", x1, ", ", y1, ")")
