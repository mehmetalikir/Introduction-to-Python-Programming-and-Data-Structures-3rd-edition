# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Pattern recognition: consecutive characters in string) Write the following
function that tests whether the string has consecutive character or not:

    def hasConsecutiveChar(string):

Write a test program that prompts the user to enter a string and reports whether it
contains consecutive characters or not.'''

def main():
    s = input("Please enter s string: ")
    if hasConsecutiveChar(s):
        print("The string has consecutive characters")
    else:
        print("The string has not consecutive characters")

def hasConsecutiveChar(string):
    # Extract items from the string
    lst = [x for x in string]

    # Whether it contains consecutive characters or not
    for i in range(0, len(lst) -1):
        if lst[i] == lst[i + 1]:
            return True

    return False


main() # Invoke main function

