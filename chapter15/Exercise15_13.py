# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the number of uppercase letters in a string) Write a recursive function to
return the number of uppercase letters in a string using the following function
headers:

    def countUppercase(s):
    def countUppercaseHelper(s, high):

Write a test program that prompts the user to enter a string and displays the number
of uppercase letters in the string.'''


def main():
    # Prompt the user to enter a string
    s = input("Please enter a string: ")

    # Display the number of uppercase letters in the string
    print(f"The number of uppercase letters in {s} is {countUppercase(s)}")


# Function counts the uppercase letters in a string
def countUppercase(s):
    return countUppercaseHelper(s, len(s) - 1)


# Helper Function
def countUppercaseHelper(s, high):
    if high < 0:  # Base case
        return 0
    count = countUppercaseHelper(s, high - 1)  # Recursive call
    if s[high].isupper():
        count += 1
    return count


main()
