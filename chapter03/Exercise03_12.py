# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Check a number) Write a program that prompts the user to enter an integer
and checks whether the number is divisible by both 2 and 3, divisible by 2
or 3, or just one of them(but not both)'''

# Prompts the user for input
number = int(input("Please enter an integer: "))

# Check the number
if number % 6 == 0:
    print("Is", number, "divisible by 2 and 3 ? True")
else:
    print("Is", number, "divisible by 2 and 3 ? False")
if number % 2 == 0 or number % 3 == 0:
    print("Is", number, "divisible by 2 or 3 ? True")
else:
    print("Is", number, "divisible by 2 or 3 ? False")
if number % 6 != 0 and number % 2 == 0 or number % 3 == 0:
    print("Is", number, "divisible by 2 or 3, but not both? False")
else:
    print("Is", number, "divisible by 2 or 3, but not both? True")


