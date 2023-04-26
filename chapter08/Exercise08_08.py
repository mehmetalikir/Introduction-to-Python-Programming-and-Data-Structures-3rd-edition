# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(All closest pairs of points) Revise Listing 8.4, FindNearestPoints.py, to find all
the nearest pairs of points that have the same minimum distance.'''

import math


def main():
    numberOfPoints = int(input("Enter the number of points: "))

    # Create a list to store points
    points = []
    for i in range(numberOfPoints):
        s = input("Enter x- and y-coordinates of point"
                  + str(i) + ": ")
        point = [float(x) for x in s.split()]
        points.append(point)

    # p1 and p2 are the indices in the points list
    p1 = 0
    p2 = 1
    list1 = [[p1, p2]]
    shortestDistances = distance(
        points[p1][0], points[p1][1],
        points[p2][0], points[p2][1])  # Initialize shortestDistances

    # Compute distance for every two points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            currentDistance = distance(
                points[i][0], points[i][1],
                points[j][0], points[j][1])

            if shortestDistances > currentDistance:
                list1 = [[i, j]]
                shortestDistances = currentDistance  # Update shortestDistances
            elif shortestDistances == currentDistance:
                list1.append([i, j])

    # Display result
    for pair in list1:
        print("The closest two points are " +
              "(" + str(points[pair[0]]) + ", " + str(points[pair[1]]) + ")")


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


main() # Invoke main function
