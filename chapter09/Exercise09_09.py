# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: intersecting point) Suppose two line segments intersect. The two
 endpoints for the first line segment are (x1, y1) and (x2, y2) and for the
 second line segment are (x3, y3) and (x4, y4). Write a program that prompts
 the user to enter these four endpoints and displays the intersecting point.
 (Hint: Use the LinearEquation class from Programming Exercise 9.7.'''

from chapter09.Exercise09_07 import LinearEquation  # import LinearEquation object


def main():

    x1 = input("Please enter the x-coordinate of point1: ")
    y1 = input("Please enter the x-coordinate of point2: ")
    x2 = input("Please enter the x-coordinate of point3: ")
    y2 = input("Please enter the x-coordinate of point4: ")
    x3 = input("Please enter the x-coordinate of point5: ")
    y3 = input("Please enter the x-coordinate of point6: ")
    x4 = input("Please enter the x-coordinate of point7: ")
    y4 = input("Please enter the x-coordinate of point8: ")

    a = y1 - y2
    b = -1 * (x1 - x2)
    c = y3 - y4
    d = -1 * (x3 - x4)
    e = (y1 - y2) * x1 - (x1 - x2) * y1
    f = (y3 - y4) * x3 - (x3 - x4) * y3

    equation = LinearEquation(a, b, c, d, e, f)

    # Solve the linear equation and display result
    if equation.isSolvable() == 0:
        print("The two lines are parallel.")
    else:
        x = equation.getX()
        y = equation.getY()
        print(f"The intersecting point is at ({x, y})")


main()  # Call the main function
