# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Format an integer) Write a function with the following header to format the
integer with the specified width.

def format(number, width):

The function returns a string for the number with one or more prefix 0s. The size
of the string is the width. For example, format(34, 4) returns 0034 and format(
34, 5) returns 00034. If the number is longer than the width, the function returns the
string representation for the number. For example, format(34, 1) returns 34.
    Write a test program that prompts the user to enter a number and its width and
displays a string returned by invoking format(number, width).'''


def format(number, width):
    # Convert the value into a string
    number = str(number)

    # Convert the value into an integer
    width = int(width)

    if len(number) > width: # Return number if the number is longer than the width
        return number
    else:
        # Assign value for prefix 0s
        zeros = ""
        for i in range(0, width - len(number), +1):
            zeros += "0"

    # Display result
    print(zeros + number)


def main():
    # Prompt the user to enter a number and its width
    number = int(input("Please enter an integer: "))
    width = input("Please enter the width: ")

    format(number, width)  # Invoke function


main()  # Call main function
