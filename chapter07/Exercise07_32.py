# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Remove non-alpha characters in a string) Write a function that returns an alpha
only string using the following header:

    def alphaOnly(s):

For example, alphaOnly("h3llo") returns hllo. Write a test program that
prompts the user to enter a string and displays the alpha only string'''


def main():
    # Prompt the user to enter a string
    s = input("Please enter a string: ")  # h3llo w0rld

    # Remove non-alpha characters in a string
    lst = alphaOnly(s)

    # Display the alpha only string
    print("The alpha only string is ", end=""), displayResult(lst)


# Returns an alpha only string
def alphaOnly(s):
    # Create an empty list
    lst = []

    for i in range(0, len(s)):
        if s[i].isalpha():
            lst.append(s[i])

    return lst


# Display result
def displayResult(lst):
    for i in range(len(lst)):
        print(lst[i], end="")


main()  # Call main function
