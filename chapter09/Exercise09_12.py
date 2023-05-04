# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: The Circle2D class) Define the Circle2D class that contains:

    ■ Two private float data fields named x and y that specify the center of the circle
    with getter/setter methods.
    ■ A private data field radius with getter/setter methods.
    ■ A constructor that creates a circle with the specified x, y, and radius. The
    default values are all 0.
    ■ A method getArea() that returns the area of the circle.
    ■ A method getPerimeter() that returns the perimeter of the circle.
    ■ A method containsPoint(x, y) that returns True if the specified point (x,
    y) is inside this circle (see Figure 9.14a).
    ■ A method contains(circle2D) that returns True if the specified circle is
    inside this circle (see Figure 9.14b).
    ■ A method overlaps(circle2D) that returns True if the specified circle
    overlaps with this circle (see Figure 9.14c).
    ■ Implement the __contains__(another) method that returns True if this
    circle is contained in another circle.
    ■ Implement the __cmp__, __lt__, __le__, __eq__, __ne__, __gt__,
    __ge__ methods that compare two circles based on their radius.

Draw the UML diagram for the class, and then implement the class. Write a test
program that prompts the user to enter two circles with x- and y-coordinates and the
radius, creates two Circle2D objects c1 and c2, displays their areas and perimeters,
and displays the result of c1.containsPoint(c2.getX(), c2.getY()),
c1.contains(c2), and c1.overlaps(c2), and the result of c1 < c2'''

import math


def main():
    x1 = float(input("Enter the center x-coordinate of c1: "))
    y1 = float(input("Enter the center y-coordinate of c1: "))
    radius1 = float(input("Enter the radius of c1: "))
    x2 = float(input("Enter the center x-coordinate of c2: "))
    y2 = float(input("Enter the center y-coordinate of c2: "))
    radius2 = float(input("Enter the radius of c2: "))

    # Create a Point object 1
    c1 = Circle2D(x1, y1, radius1)

    # Create a Point object 2
    c2 = Circle2D(x2, y2, radius2)

    print("Area for c1 is", c1.getArea())
    print("Perimeter for c1 is", c1.getPerimeter())

    print("Area for c2 is", c2.getArea())
    print("Perimeter for c2 is", c2.getPerimeter())

    print("c1 contains the center of c2?",
          c1.containsPoint(c2.getX(), c2.getY()))
    print("c1 contains c2?", c1.contains(c2))
    print("c2 in c1?", c2 in c1)
    print("c1 overlaps c2?", c1.overlaps(c2))

    print("c1 < c2?", c1 < c2)


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


class Circle2D:
    # Construct a Circle2D object
    def __init__(self, x=0.0, y=0.0, radius=0.0):
        self.__x = x
        self.__y = y
        self.__radius = radius

    # The accessor functions
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRadius(self):
        return self.__radius

    # The mutator functions
    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setRadius(self, radius):
        self.__radius = radius

    # Get perimeter of the circle.
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    # Get area of the circle.
    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def containsPoint(self, x, y):
        d = distance(x, y, self.__x, self.__y)
        return d <= self.__radius

    def contains(self, circle):
        d = distance(self.__x, self.__y, circle.__x, circle.__y)
        return d + circle.__radius <= self.__radius

    def overlaps(self, circle):
        return distance(self.__x, self.__y, circle.__x, circle.__y) \
               <= self.__radius + circle.__radius

    def __contains__(self, anotherCircle):
        return self.contains(anotherCircle)

    def __lt__(self, secondCircle):
        return self.__cmp__(secondCircle) < 0

    def __le__(self, secondCircle):
        return self.__cmp__(secondCircle) <= 0

    def __gt__(self, secondCircle):
        return self.__cmp__(secondCircle) > 0

    def __ge__(self, secondCircle):
        return self.__cmp__(secondCircle) >= 0

    # Compare two numbers
    def __cmp__(self, secondCircle):
        if self.__radius > secondCircle.__radius:
            return 1
        elif self.__radius < secondCircle.__radius:
            return -1
        else:
            return 0


main()  # Call the main function
