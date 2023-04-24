# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Area of convex polygon) A polygon is convex if it contains any line segments
 that connects two points of polygon. Write a program that prompts the user to enter the points
 counter-clockwise in one line, and displays the area of the
 polygon. For the formula for computing the area of a polygon,
 see https://www.mathwords.com/a/area_convex_polygon.htm
 '''
import math


def main():
    # Prompt the user to enter the points counter-clockwise in one line
    s = input("Please enter the coordinates of the points: ")  # -12 0 -8.5 10 0 11.4 5.5 1.8 6 -5.5 0 -7 -3.5 -5.5

    # Display result
    print(f"The total area is {getArea(s)}")


# Compute total area of polygon
def getArea(s):
    # Convert input to float
    lst = [float(x) for x in s.split(" ")]

    # Create empty lists
    x = []
    y = []

    # Extract x and y coordinates from list
    for i in range(0, len(lst), +2):
        x.append(lst[i])
        y.append(lst[i + 1])

    # Assign value
    convex = 0

    for i in range(0, len(x) - 1):
        convex += x[i] * y[i + 1]

    area = (1 / 2) * ((x[len(x) -1] * y[0]) + convex)

    return math.fabs(area)


main()  # Call main function
