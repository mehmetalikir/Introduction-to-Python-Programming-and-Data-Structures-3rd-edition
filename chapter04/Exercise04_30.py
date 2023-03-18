# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Hex to decimal) Write a program that prompts the user to enter a hex character
and displays its corresponding decimal integer'''

import sys

hexCharacter = str(input("Please enter a hex character: "))
ch = hexCharacter[0]

# Check if the hex character has exactly one character
if len(hexCharacter) != 1:
    print("You must enter exactly one character")
    sys.exit(1)

# Display decimal value for the hex digit
if 'F' >= ch >= 'A':
    value = (ord(ch) - ord('A')) + 10
    print("The decimal value", ch, " is ", value)
elif ch.isdigit():
    print("The decimal value", ch, " is ", ch)
else:
    print(ch, " is an invalid input")
