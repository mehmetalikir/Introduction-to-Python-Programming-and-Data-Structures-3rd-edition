# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Algebra: solve quadratic equations) Rewrite Programming Exercise 3.1 to obtain
imaginary roots if the determinant is less than 0 using the Complex class in
Programming Exercise 9.15.'''

import math

from Complex import Complex

a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))

discriminant = b * b - 4 * a * c

if discriminant < 0:
    r1 = Complex(-b / (2 * a), math.sqrt(-discriminant) / (2 * a))
    r2 = Complex(-b / (2 * a), math.sqrt(-discriminant) / (2 * a))
    print("The roots are", r1, "and", r2)
elif discriminant == 0:
    r1 = -b / (2 * a)
    print("The root is " + str(r1))
else:
    # (discriminant > 0)
    r1 = (-b + discriminant ** 0.5) / (2 * a)
    r2 = (-b - discriminant ** 0.5) / (2 * a)
    print("The roots are", r1, "and", r2)
