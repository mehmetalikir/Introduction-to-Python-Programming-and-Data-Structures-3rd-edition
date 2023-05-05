# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Algebra: vertex form equations) The equation of a parabola can be expressed
 in either standard form (y = ax^2 + bx + c) or vertex form (y = a(x - h)^2 + k)
 Write a program that prompts the user to enter a, b, and c as integers in
 standard form and displays h and k in the vertex form.'''
import math

import Rational

# Prompt the user to enter a, b and c
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))

a = Rational.Rational(a, 1)
b = Rational.Rational(b, 1)
c = Rational.Rational(c, 1)

# Compute h = -b / 2a and k = 4ac - b^2 / 2a
h = Rational.Rational(-b.__getitem__(0), 2 * a.__getitem__(a))

k = 0

print(f"h is {h} k is {k}")
