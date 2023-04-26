# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Points nearest to each other) The program in Listing 8.3 finds the two points in a
two-dimensional space nearest to each other. Revise the program so that it finds the
two points in a three-dimensional space nearest to each other. Use a two-dimensional
list to represent the points. Test the program using the following points:
points = [[-1, 0, 3], [-1, -1, -1], [4, 1, 1],
[2, 0.5, 9], [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2],
[5.5, 4, -0.5]]

The formula for computing the distance between two points (x1, y1, z1) and
(x2, y2, z2) in a three-dimensional space is √(x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2.'''
import math


def main():
    # Create a list
    points = [[-1, 0, 3], [-1, -1, -1], [4, 1, 1],
              [2, 0.5, 9], [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2],
              [5.5, 4, -0.5]]

    getDistance(points) # Invoke function


# Find the two points in a three-dimensional space nearest to each other
def getDistance(points):
    # Assign values
    p1, p2, p3 = 0, 1, 3

    shortestDistance = computeDistance(points[p1][0], points[p1][1],
                                       points[p2][0], points[p2][1],
                                       points[p3][0], points[p3][1])

    # Compute distance for every three points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(i + 1, len(points)):
                distance = computeDistance(points[i][0], points[i][1],
                                           points[j][0], points[j][1],
                                           points[k][0], points[k][1])

                if shortestDistance > distance:
                    p1, p2, p3 = i, j, k
                    shortestDistance = distance

    # Display result
    print(
        f"The closest three points are "
        f"({points[p1][0]},{points[p1][1]}) "
        f"({points[p2][0]},{points[p2][1]}) and "
        f"({points[p3][0]},{points[p3][1]}) ")


# Compute formula for the distance between two points
def computeDistance(x1, y1, z1, x2, y2, z2):
    distance = math.sqrt(math.pow(x2 - x1, 2) +
                         math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2))

    return distance


main()  # Invoke main function
