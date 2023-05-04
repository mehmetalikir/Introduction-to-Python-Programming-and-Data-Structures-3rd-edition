# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: The Rectangle2D class) Define the Rectangle2D class that
contains:

    ■ Two float data fields named x and y that specify the center of the rectangle
    with getter/setter methods. (Assume that the rectangle sides are parallel to x- or y- axes.)
    ■ The data fields width and height with getter/setter methods.
    ■ A constructor that creates a rectangle with the specified x, y, width, and
    height with default values 0.
    ■ A method getArea() that returns the area of the rectangle.
    ■ A method getPerimeter() that returns the perimeter of the rectangle.
    ■ A method containsPoint(x, y) that returns True if the specified point (x,
    y) is inside this rectangle (see Figure 9.15a).
    ■ A method contains(Rectangle2D) that returns True if the specified
    rectangle is inside this rectangle (see Figure 9.15b).
    ■ A method overlaps(Rectangle2D) that returns True if the specified
    rectangle overlaps with this rectangle (see Figure 9.15c).
    ■ Implement the __contains__(another) method that returns True if this
    rectangle is contained in another rectangle.
    ■ Implement the _ _cmp__, __lt__, __le_ _, __eq_ _, __ne__, __gt__,
    __ge__ methods that compare two circles based on their areas

Draw the UML diagram for the class, and then implement the class. Write a test program
that prompts the user to enter two rectangles with center x-, y-coordinates,
width, and height, creates two Rectangle2D objects r1 and r2, displays their areas
and perimeters, and displays the result of r1.containsPoint(r2.getX(),
r2.getY()), r1.contains(r2), and r1.overlaps(r2) and the result of c1 < c2'''

import math


def main():
    x1 = float(input("Please enter the center x-coordinate of r1: "))
    y1 = float(input("Please enter the center y-coordinate of r1: "))
    r1width = float(input("Please enter the width of r1: "))
    r1Height = float(input("Please enter the height of r1: "))

    x2 = float(input("Please enter the center x-coordinate of r2: "))
    y2 = float(input("Please enter the center y-coordinate of r2: "))
    r2width = float(input("Please enter the width of r2: "))
    r2Height = float(input("Please enter the height of r2: "))

    # Create a Point object 1
    r1 = Rectangle2D(x1, y1, r1width, r1Height)

    # Create a Point object 2
    r2 = Rectangle2D(x2, y2, r2width, r2Height)

    print("Area for cr is", r1.getArea())
    print("Perimeter for r1 is", r1.getPerimeter())

    print("Area for r2 is", r2.getArea())
    print("Perimeter for r2 is", r2.getPerimeter())

    print("r1 contains the center of r2?",
          r1.containsPoint(r2.getX(), r2.getY()))
    print("r1 contains r2?", r1.contains(r2))
    print("r2 in r1?", r2 in r1)
    print("r1 overlaps r2?", r1.overlaps(r2))

    print("r1 < r2?", r1 < r2)


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


class Rectangle2D:
    # Construct a Rectangle2D object
    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0):
        self.__x = x
        self.__y = y
        self.width = width
        self.height = height

    # The accessor functions
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    # The mutator functions
    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    # Get perimeter of the rectangle.
    def getPerimeter(self):
        return 2 * (self.width + self.height)

    # Get area of the rectangle.
    def getArea(self):
        return self.width * self.height

    def containsPoint(self, x, y):
        d = distance(x, y, self.__x, self.__y)
        return d >= self.hipotenus()

    def contains(self, rectangle):
        d = distance(self.__x, self.__y, rectangle.__x, rectangle.__y)
        return d + rectangle.hipotenus() >= self.hipotenus()

    def overlaps(self, rectangle):
        return distance(self.__x, self.__y, rectangle.__x, rectangle.__y) \
               >= rectangle.hipotenus() + self.hipotenus()

    def hipotenus(self):
        return math.pow(self.getWidth(), 2) + math.pow(self.getHeight(), 2)

    def __contains__(self, anotherRectangle):
        return self.contains(anotherRectangle)

    def __lt__(self, secondRectangle):
        return self.__cmp__(secondRectangle) < 0

    def __le__(self, secondRectangle):
        return self.__cmp__(secondRectangle) <= 0

    def __gt__(self, secondRectangle):
        return self.__cmp__(secondRectangle) > 0

    def __ge__(self, secondRectangle):
        return self.__cmp__(secondRectangle) >= 0

    # Compare two numbers
    def __cmp__(self, secondRectangle):
        if self.hipotenus() > secondRectangle.hipotenus():
            return 1
        elif self.hipotenus() < secondRectangle.hipotenus():
            return -1
        else:
            return 0


main()  # Call the main function
