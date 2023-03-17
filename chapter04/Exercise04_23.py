# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(pH calculator) Write a program that prompts the user to enter a number in range
of 1 - 14 and displays a message as acidic (less than 7), neutral(7) or alkaline
(more than 7), otherwise invalid if the input iso ut of range'''

# Prompt the user to enter a number in range of 1 - 14
num = float(input("Please enter a pH value between 1 to 14: "))

# Display result
if num < 7 and num >= 1:
    print(f"{num} is acidic")
elif num == 7:
    print(f"{num} is neutral")
elif num > 7 and num <= 14:
    print(f"{num} is alkaline")
else:
    print(f"{num} is invalid")
