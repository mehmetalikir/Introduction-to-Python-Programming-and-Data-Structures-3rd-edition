# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display the ASCII character table) Write a program that prints the characters in
the ASCII character table from ! to ~. Display ten characters per line. The ASCII
table is shown in Appendix B. Characters are separated by exactly one space.'''

# Constant
PER_LINE = 10

# Count the number of characters
count = 0

# Prints the characters in the ASCII character table from ! to ~
for i in range(ord('!'), ord('~')):
    print(" ", chr(i), end = "")
    count += 1
    if count == PER_LINE: # Display ten characters per line
        count = 0
        print()




