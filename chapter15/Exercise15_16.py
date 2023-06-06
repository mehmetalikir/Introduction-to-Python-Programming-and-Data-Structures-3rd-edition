# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Occurrences of a specified character in a list) Write a recursive function that finds
the number of occurrences of a specified character in a list. You need to define the
following two functions. The second one is a recursive helper function.

    def count(chars, ch):
    def countHelper(chars, ch, high):

Write a test program that prompts the user to enter a list of characters in one line,
and a character, and displays the number of occurrences of the character in the list.'''


def main():
    # Prompt the user to enter the characters
    s = input("Please enter characters separated by spaces from one line: ").strip()
    items = s.split()  # Extracts items from the string
    ch = input("Please enter a character: ").strip()

    # Display the number of occurrences of the character
    print("The number of occurrence of character " + ch + " in " + str(items) + " is " + str(count(items, ch)))


# Count the number of occurrences of a specified character in a list
def count(chars, ch):
    return countHelper(chars, ch, len(chars) - 1)


# Helper function
def countHelper(chars, ch, high):
    if high >= 0:  # Base case
        return countHelper(chars, ch, high - 1) + (1 if chars[high] == ch else 0)  # Recursive call
    else:
        return 0


main()
