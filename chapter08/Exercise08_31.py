# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: intersecting point) Write a function that returns the intersecting point of
two lines. The intersecting point of the two lines can be found by using the formula
shown in Exercise 3.25. Assume that (x1, y1) and (x2, y2) are the two points on line
1 and (x3, y3) and (x4, y4) are the two points on line 2. The function header is:

    def getIntersectingPoint(points):

The points are stored in the two-dimensional list points, with
(points[0][0], points[0][1]) for (x1, y1). The function returns the intersecting
point (x, y) in a list, and None if the two lines are parallel. Write a program
that prompts the user to enter four points and displays the intersecting point.'''


def main():
    # Prompt the user to enter a00, a01, a10, a11, b0, and b1
    x1 = float(input("Please enter x1: "))
    y1 = float(input("Please enter y1: "))
    x2 = float(input("Please enter x2: "))
    y2 = float(input("Please enter y2: "))
    x3 = float(input("Please enter x3: "))
    y3 = float(input("Please enter y3: "))
    x4 = float(input("Please enter x4: "))
    y4 = float(input("Please enter y4: "))

    # Create a list
    points = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]

    # Display the result
    if getIntersectingPoint(points) is None:
        print("The two lines are parallel")
    else:
        print(f"The intersecting point is at {getIntersectingPoint(points)}")


# Compute the intersecting point of two lines
def getIntersectingPoint(points):
    # Assign values
    x = 0
    y = 0

    a = points[0][1] - points[1][1]

    b = -1 * (points[0][0] - points[1][0])

    c = points[2][1] - points[3][1]

    d = -1 * (points[2][0] - points[3][0])

    e = a * points[0][0] - (points[0][0] - points[1][0]) * points[0][1]

    f = c * points[2][0] - (points[2][0] - points[3][0]) * points[2][1]

    disc = a * d - b * c
    x = (e * d - b * f) / disc
    y = (a * f - e * c) / disc

    if disc == 0:
        return None

    return x, y # Return values


main()  # Invoke main function
