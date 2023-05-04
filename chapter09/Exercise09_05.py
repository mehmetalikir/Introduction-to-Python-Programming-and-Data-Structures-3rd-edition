# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: n-sided regular polygon) An n-sided regular polygon’s sides all have
the same length and all of its angles have the same degree (i.e., the polygon is
both equilateral and equiangular). Design a class named RegularPolygon that
contains:

    ■ A private int data field named n that defines the number of sides in the polygon.
    ■ A private float data field named side that stores the length of the side.
    ■ A private float data field named x that defines the x-coordinate of the center of
    the polygon with default value 0.
    ■ A private float data field named y that defines the y-coordinate of the center of
    the polygon with default value 0.
    ■ A constructor that creates a regular polygon with the specified n (default 3),
    side (default 1), x (default 0), and y (default 0).
    ■ The accessor and mutator methods for all data fields.
    ■ The method getPerimeter() that returns the perimeter of the polygon.
    ■ The method getArea() that returns the area of the polygon. The formula for
    computing the area of a regular polygon is area = n x s^2 / 4 x tan(pi / n)

Draw the UML diagram for the class, and then implement the class. Write a test program
that creates three RegularPolygon objects, created using RegularPolygon(),
using RegularPolygon(6, 4) and RegularPolygon(10, 4, 5.6, 7.8). For
each object, display its perimeter and area.'''
import math


class RegularPolygon:
    # Construct a RegularPolygon object
    def __init__(self, n=3, side=1, x=0.0, y=0.0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    # The accessor functions
    def getN(self):
        return self.__n

    def getSide(self):
        return self.__side

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    # The mutator functions
    def setN(self):
        return self.__n

    def setSide(self):
        return self.__side

    def setX(self):
        return self.__x

    def setY(self):
        return self.__y

    # Get the perimeter of the polygon
    def getPerimeter(self):
        return self.getN() * self.getSide()

    # Get the area of the polygon
    def getArea(self):
        return self.getN() * self.getSide() * self.getSide() / \
               4 * math.tan(math.pi / self.getN())


# Display properties
def displayProperties(p):
    print("The are of polygon:", p.getArea(), "\nThe perimeter of polygon:", p.getPerimeter())


def main():
    # Create a Car object
    print("Object 1")
    rp0 = RegularPolygon(6, 4)
    displayProperties(rp0)

    # Create a Car object
    print("Object 2")
    rp1 = RegularPolygon(10, 4, 5.6, 7.8)
    displayProperties(rp1)


main()  # Call the main function
