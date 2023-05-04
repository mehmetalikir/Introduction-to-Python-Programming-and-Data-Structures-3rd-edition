# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Math: The Complex class) Python has the complex class for performing complex
number arithmetic. In this exercise, you will design and implement your own
Complex class. Note that the complex class in Python is named in lowercase, but
our custom Complex class is named with C in uppercase.
    A complex number is a number of the form where a and b are real numbers
and iis The numbers a and b are known as the real part and the imaginary
part of the complex number, respectively. You can perform addition, subtraction,
multiplication, and division for complex numbers using the following formulas:
You can also obtain the absolute value for a complex number using the following
formulas:
                    a + bi + c + di = (a + c) + (b + d)i
                   a + bi - (c + di) = (a - c) + (b - d)i
                 (a + bi)*(c + di) = (ac - bd) + (bc + ad)i
         (a + bi)/(c + di) = (ac + bd)/(c2 + d2) + (bc - ad)i/(c2 + d2)

You can also obtain the absolute value for a complex number using the following
formula:

                            |a + bi| = √(a^2 + b^2)

(A complex number can be interpreted as a point on a plane by identifying the (a,b)
values as the coordinates of the point. The absolute value of the complex number
corresponds to the distance of the point to the origin, as shown in Figure 9.16.)

Design a class named Complex for representing complex numbers and the methods
__add__, __sub__, __mul__, __truediv__, and __abs__ for performing
complex-number operations, and override the __str__ method by
returning a string representation for a complex number. The __str__ method
returns (a + bi) as a string. If b is 0, it simply returns a.
Provide a constructor Complex(a, b) to create a complex number with
the default value of 0 for a and b. Also provide the getRealPart() and
getImaginaryPart() methods for returning the real and imaginary parts of the
complex number, respectively.
Write a test program that prompts the user to enter two complex numbers and displays
the result of their addition, subtraction, multiplication, and division
'''

from Complex import Complex

r1 = float(input("Please enter the real part of the first complex number: "))
i1 = float(input("Please enter the imaginary part of the first complex number: "))
com1 = Complex(r1, i1)

r2 = float(input("Please enter the real part of the second complex number: "))
i2 = float(input("Please enter the imaginary part of the second complex number: "))
com2 = Complex(r2, i2)

print(f"{com1.__str__()} + {com2.__str__()} = {com1.__add__(com2)}")
print(f"{com1.__str__()} - {com2.__str__()} = {com1.__sub__(com2)}")
print(f"{com1.__str__()} / {com2.__str__()} = {com1.__mul__(com2)}")
print(f"{com1.__str__()} * {com2.__str__()} = {com1.__truediv__(com2)}")
print(f"|{com1.__str__()}| = {com1.__abs__()}")
