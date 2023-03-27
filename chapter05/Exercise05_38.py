# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(The Longest common prefix) Write a program that prompts the user to enter two
strings and displays the largest common prefix of the two strings. If the two
strings have no common prefix, display No common prefix.'''

# Prompt the user to enter two strings
s1 = input("PLease enter s1: ")
s2 = input("PLease enter s2: ")
prefix = ""

# Get the largest common prefix of the two strings
for i in range(0, len(s1), +1):
    if s1[i] == s2[i]:
        if s1[i] != s2[i]: # Stop assigning to prefix
            break
        prefix += s1[i]
    else:
        "No common prefix"

# Display result
print("The common prefix is", prefix)
