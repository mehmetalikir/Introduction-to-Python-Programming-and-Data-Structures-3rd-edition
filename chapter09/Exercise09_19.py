# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Parse complex numbers) Add the following non-member function in the
Complex class defined in Programming Exercise 9.15.

    def parseComplexNumber(s):

The function returns a Complex object from a string that represents a complex
number. Here are some examples of parsing complex numbers:

    c1 = parseComplexNumber("3.5 + 2.23i")
    c2 = parseComplexNumber("3.5") # Imaginary part is 0
    c3 = parseComplexNumber("-2.23i") # Real part is 0
    c4 = parseComplexNumber("3.5 - 2.23i") # This is K

Write a test program that prompts th user to enter complex numbers as
strings and displays their addition. Note that if the real part or imaginary part is
0, it is not displayed. If the imaginary part is 1, the number is not displayed.

Write a test program that prompts the use to enter two rational numbers as
strings and displays their addition'''

from Complex import *


