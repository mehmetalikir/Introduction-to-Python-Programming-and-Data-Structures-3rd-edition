# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Display characters) Write a function that prints characters using the following
header:

def printChars(ch1, ch2, numberPerLine)

This function prints the characters between ch1 and ch2 with the specified numbers
per line. Write a test program that prints ten characters per line from 1 to Z.
Characters are separated by exactly one space.'''

# Print ten characters per line from 1 to Z
def printChars(ch1, ch2, numberPerLine):

    count = 0 # Count the number of breaks per line

    # Display result
    for i in range(ord('1'), ord('Z')+1, +1):
        print(chr(i), end=" ") # Print in line by exactly one space
        count += 1
        if count % numberPerLine == 0:
            print() # Break line

def main():
    printChars('1', 'Z', 10)

main()
