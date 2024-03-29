# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Turtle: Contex hull using Graham's algorithm) Extend Programing Exercise
16.12 to display the points and their convex hull using Turtle, a shown in
Figure 16.16'''

import math
import turtle

from chapter15.Exercise15_36 import drawLine


# Return the points that form a convex hull
def getConvexHull(myPoints):
    # Step 1
    h0 = getRightmostLowestPoint(myPoints)

    H = [h0]
    t0 = h0

    # Step 2 and Step 3
    while True:
        t1 = myPoints[0]
        for i in range(1, len(myPoints)):
            status = whichSide(t0[0], t0[1], t1[0], t1[1], myPoints[i][0], myPoints[i][1])

            if status < 0:  # Right side of the line
                t1 = myPoints[i]
            elif status == 0:
                if distance(myPoints[i][0], myPoints[i][1], t0[0], t0[1]) > distance(t1[0], t1[1], t0[0], t0[1]):
                    t1 = myPoints[i]

        if t1[0] == h0[0] and t1[1] == h0[1]:
            break  # A convex hull is found
        else:
            H.append(t1)
            t0 = t1

    return H


# Return the rightmost lowest point in S
def getRightmostLowestPoint(p):
    rightMostIndex = 0
    rightMostX = p[0][0]
    rightMostY = p[0][1]

    for i in range(1, len(p)):
        if rightMostY > p[i][1]:
            rightMostY = p[i][1]
            rightMostX = p[i][0]
            rightMostIndex = i
        elif rightMostY == p[i][1] and rightMostX < p[i][0]:
            rightMostX = p[i][0]
            rightMostIndex = i

    return p[rightMostIndex]


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


# Is (x2, y2) on the right side of [x0, y0] and [x1, y1]
def whichSide(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)


def drawPoints(points):
    for p in points:
        turtle.penup()
        turtle.goto(p[0], p[1] - 2)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(2)
        turtle.end_fill()


# Draw a polyline to connect all the points in the list
def drawPolyline(points):
    for i in range(len(points) - 1):
        drawLine(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1])


# Draw a polygon to connect all the points in the list and
# close the polygon by connecting the first point with the last point
def drawPolygon(points):
    drawPolyline(points)
    from chapter15.Exercise15_36 import drawLine
    drawLine(points[len(points) - 1][0], points[len(points) - 1][1], points[0][0], points[0][1])  # Close the polygon


# Fill a polygon by connecting all the points in the list
def fillPolygon(points):
    turtle.begin_fill()
    drawPolygon(points)
    turtle.end_fill()


coordinates = input("Please enter the points: ")
c = coordinates.split()
points = [[float(c[i]), float(c[i + 1])] for i in range(0, len(c), 2)]

drawPoints(points)

convexHull = getConvexHull(points)
print("The convex hull is ")
print(convexHull)
drawPolygon(convexHull)

turtle.hideturtle()

turtle.done()
