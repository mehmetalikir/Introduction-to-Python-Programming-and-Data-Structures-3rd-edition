# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Check substrings) You can check whether a string is a substring of another string
by using the find method(function) in the str class. Write the following function to check
whether string s1 is a substring of string s2. The function returns the first index
in s2 if there is a match. Otherwise, return -1

def indexOf(s1, s2)

Write a test program that reads two stings and checks whether the first string is
a substring of the second string. '''

def main():
    # Prompt the user to enter strings
    s1= input("Please enter a string for s1: ")
    s2 = input("Please enter a string for s2: ")

    # Display result
    print(indexOf(s1,s2))

# Check whether the first string is a substring of the second string
def indexOf(s1, s2):
    if s2.find(s1):
        return s1[0] # Return the first index
    else:
        return -1 # Otherwise, return -1

main()



