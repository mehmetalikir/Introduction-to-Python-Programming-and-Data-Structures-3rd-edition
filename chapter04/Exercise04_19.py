# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the binary code of a character) Write a program that receives a character and
displays its binary code.'''


# Prompt the user to enter a character
c = (input("Please enter a character: "))

# Display result
print(f"The binary code of {c} is",'{:0b}'.format(ord(c)))

