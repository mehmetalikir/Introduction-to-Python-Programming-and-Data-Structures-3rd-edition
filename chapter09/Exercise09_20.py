# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Parse rational numbers) Write the following function that returns a Rational
object from a string that represents a rational number.

    def parseRationalNumber(s)

The Rational class is defined in Listing 9.13. Here are some examples of parsing
rational numbers:
    r1 = parseRationalNumber("3 / 15")
    r2 = parseRationalNumber("-3/15") # This is OK
    r3 = parseRationalNumber(34) # Denominator is 1

Write a test program that prompts the user to enter two rational numbers as
stings and displays their addition.'''

from Rational import *

def removeBlank(s):
    result = ""
    for ch in s:
        if ch != ' ':
            result += ch
    return result

def parseRationalNumber(s):
    s = removeBlank(s)
    if "/" in s:
        s1 = s[0 : s.find('/')]
        s2 = s[s.find('/') + 1 : ]
        # print("s1 ", s1, " s2 ", s2)
        return Rational(int(s1), int(s2))
    else:
        return Rational(int(s), 1)

def main():
    # r1 = parseRationalNumber(input("Please enter the first rational number: "))
    # r2 = parseRationalNumber(input("Please enter the second rational number: "))

    r1 = parseRationalNumber("3 / 15")
    r2 = parseRationalNumber("-3/15")  # This is OK
    r3 = parseRationalNumber("34")  # Denominator is 1

    print(r1, "+", r2, "=", r1 + r2)
    print(r3)

main()

