# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Algebra: solve 2 * 2 linear equations) You can use Cramer’s rule to solve
the following 2 x 2 system of linear equation:

Write a program that prompts the user to enter a, b, c, d, e, and f
and displays the result. If ad - bc is 0, report that “The equation has no
solution."'''

# Prompt the user for input
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))
d = float(input("Please enter d: "))
e = float(input("Please enter e: "))
f = float(input("Please enter f: "))

# Solve the linear equation and display result
if (a * d - b * c) == 0:
    print("The equation has no solution.")
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x is ", x, " and y is ", y)
