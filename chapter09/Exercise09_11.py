# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(The Point class) Design a class named Point to represent a point with x- and y-
coordinates. The class contains:

    ■ Two private data fields x and y that represent the coordinates with get methods.
    ■ A constructor that constructs a point with specified coordinates with default
    point (0, 0).
    ■ A method named distance that returns the distance from this point to another
    point of the Point type.
    ■ A method named isNearBy(p1) that returns true if point p1 is close to this
    point. Two points are close if their distance is less than 5.
    ■ Implement the __str__ method to return a string in the form (x, y).

Draw the UML diagram for the class, and then implement the class. Write a test
program that prompts the user to enter two points, displays the distance between
them, and indicates whether they are near each other.'''
import math


class Point:
    # Construct a Point object
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    # The accessor functions
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    # Return true if point p1 is close to this point. Two points are close if their distance is less than 5
    def isNearBy(self, p1):
        d = distance(self.__x, self.__y, p1.__x, p1.__y)
        return d < 5

    # Return a string representation
    def __str__(self):
        return str((self.__x, self.__y))


# Get the distance from this point to another point of the Point type
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


# Display properties
def displayProperties(p1, p2):
    print(f"The distance between the two points is {distance(p1.getX(), p1.getY(), p2.getX(), p2.getY())}")
    if p2.isNearBy(p1):
        print("The two points are near to each other")
    else:
        print("The two points are not near to each other")


def main():
    x1 = float(input("Please enter the x- coordinates of point1: "))
    y1 = float(input("Please enter the y- coordinates of point2: "))
    x2 = float(input("Please enter the x- coordinates of point3: "))
    y2 = float(input("Please enter the x- coordinates of point4: "))

    # Create a Point object 1
    p1 = Point(x1, y1)

    # Create a Point object 2
    p2 = Point(x2, y2)

    displayProperties(p1, p2)


main() # Call the main function

# s1 = "Melbourne"
#     print("Is M in s1", 'M' in s1)
#     print("Does M contain s1", s1.__contains__('M'))
#
#     i = 0
#     j = 1
#     print(i+j)
#     print(i.__add__(j))
