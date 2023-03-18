# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Hex to binary) Write a program that prompts the user to enter a hex digit and
displays its corresponding binary number. Display a hex digit in four binary digits.
For example, hex digit 7 is 0111 in binary. Hex digits can be entered either
in uppercase or lowercase. For an incorrect input, display invalid input.'''

import sys

hexCharacter = str(input("Please enter a hex character: "))
ch = str(hexCharacter[0])

# Check if the hex character has exactly one character
if len(hexCharacter) != 1:
    print("You must enter exactly one character")
    sys.exit(1)

# Display binary value for the hex digit
if 'A' <= ch <= 'F' or 0 <= int(ch) <= 9:
    value = ord(ch)
    print("The binary value", ch, " is ", "{0:b}".format(value))
else:
    print(ch, " is an invalid input")