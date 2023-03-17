# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Process a string) Write a program that prompts the user to enter a string and displays
its length and its last character, and total number of spaces.'''

# Prompt the user for input
s = str(input("Please enter a string: ")) # Welcome to Python Programming

# Display result
print("THe length of string is", len(s))
print("The last character of string is", s[-1])
print("Total number of spaces is",s.count(" "))