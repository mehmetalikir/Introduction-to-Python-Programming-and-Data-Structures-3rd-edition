# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Central city) Given a set of cities, the central point is the city that has the shortest
total distance to all other cities. Write a program that prompts the user to enter the
number of the cities and the locations of the cities (that is, their coordinates), and
finds the central city.'''

import math

MAX_VALUE = 1_000_000_000


def main():
    # Create a list
    points = [[2.5, 5], [5.1, 3], [1, 9],
              [5.4, 54], [5.5, 2.1]]

    getPoints(points)  # Invoke function


# Find the central city
def getPoints(points):
    # Assign values
    minSum = MAX_VALUE
    point = [0] * 2

    for i in range(len(points)):
        sum = 0
        for j in range(len(points)):
            if i != j:
                # Sum each cities' distance
                sum += computeDistance(points[i][0], points[i][1], points[j][0],points[j][1])

        if sum < minSum:
            minSum = sum
            point[0] = points[i][0]
            point[1] = points[i][1]

    # Display result
    print(f"The central city is at {point[0], point[1]}")
    print(f"Total distance to all other cities is %.2f" % minSum)


# Compute formula for the distance between two points
def computeDistance(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    return distance


main()  # Invoke main function
