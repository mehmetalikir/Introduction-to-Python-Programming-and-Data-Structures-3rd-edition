# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(The Longest common prefix) Write the prefix function using the following function
header return the longest common prefix between two strings:

def prefix(s1, s2):

Write a test program  that prompts the user to enter two strings and displays
their longest common prefix'''


def main():
    # Prompt the user to enter strings
    s1 = input("Please enter the first string: ")
    s2 = input("Please enter the second string: ")

    # Display result
    print(prefix(s1,s2))


# Return the longest common prefix between two strings
def prefix(s1, s2):
    # Assign value
    commonPrefix = ""

    # Get the longest common prefix of the two strings
    for i in range(0, len(s1), +1):
        if s1[i] == s2[i]:
            if s1[i] != s2[i]:  # Stop assigning to prefix
                break
            commonPrefix += s1[i]
        else:
           return "No common prefix"

    return "The common prefix is " + commonPrefix


main()
