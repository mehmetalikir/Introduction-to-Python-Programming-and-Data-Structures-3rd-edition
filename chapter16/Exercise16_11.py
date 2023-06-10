# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: Gift-wrapping algorithm for funding a convex hull) Section 16.10.1
introducing the gift-wrapping algorithm for funding a convex hull for a set of
points. Implement the algorithm using the following function.

    # Return the points that from a convex hull
    def getConvexHull(points):

Write a test program that prompt the user to enter the set size and points
and displays the points that from a convex hull. Hint: Use your IDE to debug the
code. As you debug, you will discover that the algorithm overlooked the
two cases (1) when t1 = t0 and (2) when there is a point that is on the same line
from t0 to t1. When either case happens, replace t1 by point p if the distance
from t0 to p is greater than the distance from t0 to t1.'''


def main():
    points = input("Please enter the points in one line separated by space: ").split()
    points = [(float(points[i]), float(points[i + 1])) for i in range(0, len(points), 2)]

    convexHull = getConvexHull(points)
    print("The convex hull is", convexHull)


# Return the points that form a convex hull
def getConvexHull(points):
    if len(points) < 3:
        return points

    # Find the leftmost point
    leftmost = min(points, key=lambda p: p[0])
    hull = []
    current = leftmost
    nextPoint = None

    while True:
        hull.append(current)
        nextPoint = points[0]

        for point in points[1:]:
            # Find the next point in counterclockwise order
            orientation = ccw(current, nextPoint, point)
            if (nextPoint == current) or (orientation < 0) or \
                    (orientation == 0 and distance(current, point) > distance(current, nextPoint)):
                nextPoint = point

        current = nextPoint

        if current == leftmost:
            break

    return hull


# Check the orientation of three points (ccw = counterclockwise, cw = clockwise, colinear = colinear)
def ccw(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])


# Calculate the Euclidean distance between two points
def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


main()
