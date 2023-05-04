# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Algebra: quadratic equations) Design a class named QuadraticEquation for
 a quadratic equation ax2 + bx + x = 0. The class contains:
 ■ The private data fields a, b, and c that represent three coefficients.
 ■ A constructor for the arguments for a, b, and c.
 ■ Three getter methods for a, b, and c.
 ■ A method named getDiscriminant() that returns the discriminant, which is
   b2 - 4ac.
 ■ The methods named getRoot1() and getRoot2() for returning the two roots
 of the equation using these formulas:

           r1 = (-b + √(b^2 - 4ac)) / 2a and r2 = (-b - √(b2 - 4ac)) / 2a

 These methods are useful only if the discriminant is non-negative. Let these
 methods return 0 if the discriminant is negative.
    Draw the UML diagram for the class and then implement the class. Write a test
 program that prompts the user to enter values for a, b, and c and displays the
 result based on the discriminant. If the discriminant is positive, display the
 two roots. If the discriminant is 0, display the one root. Otherwise, display
 “The equation has no roots.”'''

import math


class QuadraticEquation:
    # Construct a QuadraticEquation object
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    # The accessor functions
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    # Get the discriminant
    def getDiscriminant(self):
        return self.__b * self.__b - 4 * self.__a * self.__c

    # Get the root 1
    def getRoot1(self):
        return (-self.__b + math.sqrt(self.getDiscriminant())) / (2 * self.__a)

    # Get the root 2
    def getRoot2(self):
        return (-self.__b - math.sqrt(self.getDiscriminant())) / (2 * self.__a)


def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    equation = QuadraticEquation(a, b, c)
    discriminant = equation.getDiscriminant()

    if discriminant < 0:
        print("The equation has no roots")
    elif discriminant == 0:
        print("The root is", equation.getRoot1())
    elif discriminant >= 0:
        print("The roots are", equation.getRoot1(), "and", equation.getRoot2())
    else:
        print("Something went wrong!")


main()  # Call the main function
