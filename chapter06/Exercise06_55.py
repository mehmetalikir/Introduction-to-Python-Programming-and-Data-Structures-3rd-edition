# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Phone keypads) The international standard letter/number mapping for telephones
is:

def getNumber(uppercaseLetter):

Write a test program that prompts the user to enter a phone number as a string.
The input number may contain letters. The program translates a letter (uppercase
or lowercase) to a digit and leaves all other characters intact. Here is a sample run
of the program:'''


def main():
    # Prompt the user to enter a string, for example: 1-800-Flowers
    s = input("Please enter a string: ")

    for i in range(0, len(s), +1):
        key = chr(ord(s[i].upper()))  # Convert str to uppercase and unicode-ord then chr value

        # Display result
        print(getNumber(key), end="")  # Invoke function



def getNumber(uppercaseLetter):
    # Assign value
    key = uppercaseLetter

    if '0' <= key <= '9':
        return key

    # Translate the letter to a digit
    if key == 'A' or key == 'B' or key == 'C':
        key = 2

    elif key == 'D' or key == 'E' or key == 'F':
        key = 3

    elif key == 'G' or key == 'H' or key == 'I':
        key = 4

    elif key == 'J' or key == 'K' or key == 'L':
        key = 5

    elif key == 'M' or key == 'N' or key == 'O':
        key = 6

    elif key == 'P' or key == 'Q' or key == 'R' or key == 'S':
        key = 7

    elif key == 'T' or key == 'U' or key == 'V':
        key = 8

    elif key == 'W' or key == 'X' or key == 'Y' or key == 'Z':
        key = 9

    return key


main()  # Call main function
