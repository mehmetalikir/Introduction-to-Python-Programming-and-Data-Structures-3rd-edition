# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Algebra: solve quadratic equations) The two roots of a quadratic equation,
for example, ax^2 + bx + c = 0 can be obtained using the following
formula:
*********************
b^2 - 4ac is called the discriminant of the quadratic equation. If it is
positive, the equation has two real roots. If it is zero, the equation has
one root. If it is negative,the equation has no real roots.Write a program
that prompts the user to enter values for a, b, and c and displays the
result based on the discriminant. If the discriminant is positive, display two
roots. If the discriminant is 0, display one root. Otherwise, display “The equation
has no real roots”.'''
import math

# Prompt the user for input
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Compute the quadratic equation and display result
discriminant = math.pow(b, 2) - 4 * a * c
if discriminant > 0:
    root1 = ((-b + (math.pow(discriminant, 0.5))) / (2 * a))
    root2 = (-b - math.pow(discriminant, 0.5)) / (2 * a)
    print("The roots are", root1, "and", root2)
elif discriminant == 0:
    root1 = (-b + math.pow(discriminant, 0.5)) / (2 * a)
    print("The root is", root1)
else:
    print("The equation has no real roots.")
