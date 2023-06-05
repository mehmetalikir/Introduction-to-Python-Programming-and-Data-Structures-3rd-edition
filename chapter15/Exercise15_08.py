# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Print the digits in an integer reversely) Write a recursive function that displays
an integer value reversely on the console using the following header:

    def reverseDisplay(value):

For example, invoking reverseDisplay(12345) displays 54321. Write a test
program that prompts the user to enter an integer and displays its reversal.'''


def main():
    # Prompt the user to enter an integer
    i = int(input("Please enter an integer: "))
    reverseDisplay(i)  # Call function


# Display an integer value reversely on the console
def reverseDisplay(value):
    if value != 0:  # Base case
        print(value % 10, end="")
        value = value // 10
        reverseDisplay(value)  # Recursive call


main()
