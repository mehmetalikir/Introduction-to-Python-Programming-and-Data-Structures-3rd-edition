# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(The Square class) Following the example of the Circle class in Section
9.2, design a class named Square to represent a rectangle. The class contains:

    ■ A data fields named side.
    ■ A constructor that creates a square with the specified side.
    The default value for the side is 1.
    ■ A method named getArea() that returns the area of this square.
    ■ A method named getPerimeter() that returns the perimeter.

Draw the UML diagram for the class, and then implement the class. Write a test
program that creates two Square objects-—one with side of 5.3 and the other
with side of 9. Display the side, area, and perimeter of each square in this order.'''


class Square:
    # Construct a square object
    def __init__(self, side=1):
        self.side = side

    def getArea(self):
        return self.side * self.side

    def getPerimeter(self):
        return 4 * self.side


def main():
    # Create a square with default value, side = 1
    square1 = Square()
    print(f"The area of the square of side {square1.side} is {square1.getArea()}")
    print(f"The perimeter of the square of side {square1.side} is {square1.getPerimeter()}")

    # Create a square with side 10
    square1 = Square(10)
    print(f"The area of the square of side {square1.side} is {square1.getArea()}")
    print(f"The perimeter of the square of side {square1.side} is {square1.getPerimeter()}")

    # Create a square with side 100
    square1 = Square(100)
    print(f"The area of the square of side {square1.side} is {square1.getArea()}")
    print(f"The perimeter of the square of side {square1.side} is {square1.getPerimeter()}")


main()  # Call the main function
