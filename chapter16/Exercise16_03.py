# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Pattern matching) Write a program that prompts the user to enter two strings
and tests whether the second string is a substring of the first string. Suppose
the neighboring characters in the string are distinct. (Don’t use the indexOf
method in the String class.) Analyze the time complexity of your algorithm.
Your algorithm needs to be at least O(n) time.'''


def isSubstring(string, substring):
    # Length of the main string and the substring
    stringLength = len(string)
    substringLength = len(substring)

    # Iterate through the main string
    for i in range(stringLength - substringLength + 1):
        # Check if the substring matches a portion of the main string
        if string[i:i + substringLength] == substring:
            return i

    return -1


# Prompt the user to enter the two strings
string1 = input("Please enter the main string: ")
string2 = input("Please enter the substring: ")

# Check if the second string is a substring of the first string
matchIndex = isSubstring(string1, string2)

if matchIndex != -1:
    print("Matched at index:", matchIndex)
else:
    print("The second string is not a substring of the first string.")
