# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: polygon subareas) A convex four-vertex polygon is divided into four
triangles, as shown in Figure 8.8.

Write a program that prompts the user to enter the coordinates of four vertices and
displays the areas of the four triangles in increasing order.'''


# from chapter08.Exercise08_31 import getIntersectingPoint
# from chapter08.Exercise08_32 import getTriangleArea

def main():
    # Prompt the user to enter coordinates o vertex
    line = input("Please enter x1, y1, x2, y2, x3, y3, x4, y4: ").split()  # -2.5 2 4 4 3 -2 -2 -3.5
    points = [[float(line[i]), float(line[i + 1])] for i in range(0, 8, 2)]

    # Get intersection points
    intersectionPoint = getIntersectingPoint(points)

    # Get triangles' coordinates from vertex TO-DO
    triangles0 = [intersectionPoint, [points[0][0], points[0][1]], [points[3][0], points[1][1]]]

    # Get area of triangles TO-DO
    print(getTriangleArea(triangles0))


# Compute the area of a triangle
def getTriangleArea(points):
    x1, y1, x2, y2, x3, y3 = points[0][0], points[0][1], \
                             points[1][0], points[1][1], points[2][0], points[2][1]

    # Compute the length of the three sides
    side1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
    side2 = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5
    side3 = ((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)) ** 0.5

    s = (side1 + side2 + side3) / 2
    temp = s * (s - side1) * (s - side2) * (s - side3)
    area = temp ** 0.5

    if temp < 0 or temp <= 0.0000000000001:
        return None
    else:
        return area


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

    disc = (a * d - b * c)
    x = (e * d - b * f) / disc
    y = (a * f - e * c) / disc

    if disc == 0:
        return None

    return [x, y]  # Return values


main()  # Invoke main function
