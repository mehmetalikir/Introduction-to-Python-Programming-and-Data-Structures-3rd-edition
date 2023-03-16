# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the character of an ASCII code) Write a program that receives an ASCII code
(an integer between 0 and 127) and displays its character.For example, if the user
enters 97, the program displays the character a'''

# Prompt the user to enter an integer between 0 and 127
num = int(input("Please enter an ASCII code: "))

# Display result
print(f"The character for ASCII code {num} is", chr(num))