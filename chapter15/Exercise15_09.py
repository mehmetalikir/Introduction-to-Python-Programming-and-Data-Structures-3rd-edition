# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Print the characters in a string reversely) Write a recursive function that displays
a string reversely on the console using the following header:

    def reverseDisplay(value):

For example, reverseDisplay("abcd") displays dcba. Write a test program
that prompts the user to enter a string and displays its reversal.'''

def main():
    # Prompt the user to enter a string
    string = input("Please enter a string: ")
    reverseDisplay(string)  # Call function


# Display a string value reversely on the console
def reverseDisplay(value):
    if len(value) > 0:  # Base case
        print(value[-1], end="")
        value = value[:-1]
        reverseDisplay(value)  # Recursive call


main()
