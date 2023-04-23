# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Algebra: solve quadratic equations) Write a function for solving a quadratic
equation using the following header:

    def solveQuadratic(eqn, roots)

The coefficients of a quadratic equation ax2 + bx + c = 0 are passed to the
list eqn and the real roots are stored in roots. The function returns the number
of real roots. See Programming Exercise 3.1 on how to solve a quadratic
equation.
    Write a program that prompts the user to enter values for a, b, and c and displays
the number of real roots and all non-complex roots.'''

import math


def main():
    eqn = [0.0] * 3
    roots = [0.0] * 3

    # Prompt the user for input
    a = float(input("Please enter a: "))
    eqn[0] = a
    b = float(input("Please enter b: "))
    eqn[1] = b
    c = float(input("Please enter c: "))
    eqn[2] = c

    solveQuadratic(eqn, roots)


def solveQuadratic(eqn, roots):
    a = eqn[0]
    b = eqn[1]
    c = eqn[2]

    # Compute the quadratic equation and display result
    discriminant = math.pow(b, 2) - 4 * a * c

    if discriminant > 0:
        roots[0] = ((-b + (math.pow(discriminant, 0.5))) / (2 * a))
        roots[1] = (-b - math.pow(discriminant, 0.5)) / (2 * a)
        print("The roots are", roots[0], "and", roots[1])

    elif discriminant == 0:
        roots[0] = (-b + math.pow(discriminant, 0.5)) / (2 * a)
        print("The root is", roots[0])

    else:
        print("The equation has no real roots.")


main()
