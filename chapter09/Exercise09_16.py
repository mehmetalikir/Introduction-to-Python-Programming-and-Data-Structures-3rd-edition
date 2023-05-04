# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Convert decimals to fractions) Write a program that prompts the user to enter
a decimal number and displays the number in a fraction. Hint: Read the decimal
number as a string, extract the integer part and fractional part from the string,
and use the Rational class to obtain a rational number for the decimal number.'''

import Rational


def getFraction(decimal):
    items = decimal.split(".")
    if len(items) <= 1:
        return decimal
    else:
        return Rational.Rational(int(items[0] + items[1]), 10 ** len(items[1]))


decimal = input("Please enter a decimal number: ")
print("The fraction number is", getFraction(decimal))
