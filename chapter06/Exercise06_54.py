# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Count the numeric in a string) Write a function that counts the numeric characters
in a string the following header:

def countNumerics(strings):

Write a test program that prompts the user to enter a string and displays the count
of numeric characters in the string'''


def main():
    # Prompt the user to enter a string and a character
    strings = input("Please enter a string: ")

    # Display result
    print(f"The count of numeric characters in {strings} is {countNumerics(strings)}")


def countNumerics(strings):
    # Assign value
    count = 0

    # Get the count of numeric characters in the string
    for i in range(0, len(strings), +1):
        if strings[i].isdigit():
            count += 1

    return count


main()  # Call main function
