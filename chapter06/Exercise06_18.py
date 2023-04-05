# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Geometry: point position) Programming Exercise 3.31 shows how to test whether
a point is on the left side of a directed line, on the right, or on the same line. Write
the functions with the following headers:

# Return true if point (x2, y2) is on the left side of the
# directed line from (x0, y0) to (x1, y1)
def leftOfTheLine(x0, y0, x1, y1, x2, y2)
# Return true if point (x2, y2) is on the same
# line from (x0, y0) to (x1, y1)
def onTheSameLine(x0, y0, x1, y1, x2, y2)
# Return true if point (x2, y2) is on the
#line segment from (x0, y0) to (x1, y1)
def onTheLineSegment(x0, y0, x1, y1, x2,y2)

Write a program that prompts the user to enter the three points for p0, p1, and p2
and displays whether p2 is on the left of the line from p0 to p1, right, the same
line, or on the line segment.'''


# Return true if point (x2, y2) is on the left side of the
# directed line from (x0, y0) to (x1, y1)
def leftOfTheLine(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) > 0

# Return true if point (x2, y2) is on the same
# line from (x0, y0) to (x1, y1)
def onTheSameLine(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) == 0

# Return true if point (x2, y2) is on the
# line segment from (x0, y0) to (x1, y1)
def onTheLineSegment(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) < 0
def main():
    # Prompt the user to enter the three points for p0, p1, and p2
    x0 = float(input("Please enter the x-coordinate of Point 0: "))
    y0 = float(input("Please enter the y-coordinate of Point 0: "))
    x1 = float(input("Please enter the x-coordinate of Point 1: "))
    y1 = float(input("Please enter the y-coordinate of Point 1: "))
    x2 = float(input("Please enter the x-coordinate of Point 2: "))
    y2 = float(input("Please enter the y-coordinate of Point 2: "))

    # Display result
    str = ""
    if leftOfTheLine:
        str = "left side of the"
    if onTheSameLine:
        str = "same line"
    if onTheLineSegment:
        str = "right side of the"

    print("(", x2, ", ", y2, ") is on the", str, "line from (", x0, ", ", y0,
          ") to (", x1, ", ", y1, ")")

main()
