# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

''''''
import turtle
from UsefulTurtleFunctions import drawLine

# Draw a polyline to connect all the points in the list
def drawPolyline(points):
    for i in range(len(points) - 1):
        drawLine(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1])

# Draw a polygon to connect all the points in the list and
# close the polygon by connecting the first point with the last point
def drawPolygon(points):
    drawPolyline(points)
    drawLine(points[len(points) - 1][0], points[len(points) - 1][1], points[0][0], points[0][1]) # Close the polygon

# Fill a polygon by connecting all the points in the list
def fillPolygon(points):
    turtle.begin_fill()
    drawPolygon(points)
    turtle.end_fill()