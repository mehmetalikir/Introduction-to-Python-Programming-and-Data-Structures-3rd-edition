# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Algebra: 2  2 linear equations) Design a class named LinearEquation for a
 2 x 2 system of linear equations:

  ax + by = e, cx + dy = f; x = (ed - bf) / (ad - bc) y = (af - ec) / (ad - bc)

 The class contains:
 ■ The private data fields a, b, c, d, e, and f with getter methods
 ■ A constructor with the arguments for a, b, c, d, e, and f.
 ■ A method named isSolvable() that returns true if ad - bc is not 0.
 ■ Methods getX() and getY() that return the solution for the equation.

 Draw the UML diagram for the class and then implement the class. Write a test
 program that prompts the user to enter a, b, c, d, e, and f and displays the
 result. If ad - bc is 0, report that “The equation has no solution.”'''


class LinearEquation:
    # Construct a LinearEquation object
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    # The accessor functions
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getF(self):
        return self.__e

    def getE(self):
        return self.__f

    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)

    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)

    def isSolvable(self):
        return (self.__a * self.__d - self.__b * self.__c)


def main():
    # Prompt the user for input
    a = float(input("Please enter a: "))
    b = float(input("Please enter b: "))
    c = float(input("Please enter c: "))
    d = float(input("Please enter d: "))
    e = float(input("Please enter e: "))
    f = float(input("Please enter f: "))
    equation = LinearEquation(a, b, c, d, e, f)

    # Solve the linear equation and display result
    if equation.isSolvable() == 0:
        print("The equation has no solution.")
    else:
        x = equation.getX()
        y = equation.getY()
        print("x is ", x, " and y is ", y)


main()  # Call the main function
