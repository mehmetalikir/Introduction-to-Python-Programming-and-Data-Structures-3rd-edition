# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(The Rectangle class) Design a class named Rectangle that extends the
GeometricObject class. The Rectangle class contains:
■ Two float data fields named width and height to denote the four
sides of the rectangle.
■ A constructor that creates a rectangle with the specified width and height
with default values 1.0.
■ The accessor methods for all two data fields.
■ A method named getArea() that returns the area of this rectangle.
■ A method named getPerimeter() that returns the perimeter of this rectangle.
■ A method named __str__() that returns a string description for the rectangle.

For the formula to compute the area of a rectangle, see Exercise 1.19. The
__str__() method is implemented as follows:

return "Rectangle: width = " + str(width) + " height = " +
str(height)

Implement the Rectangle class. Write a test program that prompts the user to
enter the two sides of the rectangle, a color, and 1 or 0 to indicate whether the triangle
is filled. The program should create a Rectangle object with these sides and
set the color and filled properties using the input. The program should display the
rectangle’s area, perimeter, color, and True or False to indicate whether the triangle
is filled or not.'''

from Rectangle import Rectangle


def main():
    # Prompt the user to enter the specifications of the rectangle
    width = float(input("Please enter width: "))
    height = float(input("Please enter height: "))
    color = input("Please enter color: ")
    filled = input("Please enter 1/0 for filled: ")

    rectangle = Rectangle(width=width, height=height)
    rectangle.setColor(color)
    isFilled = (filled == 1)
    rectangle.setFilled(isFilled)

    print(rectangle)
    print("The area is", rectangle.getArea())
    print("The perimeter is", rectangle.getPerimeter())
    print("Color is", rectangle.getColor())
    print("Filled is", rectangle.isFilled())


main()
