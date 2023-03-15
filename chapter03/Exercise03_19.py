# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Check ascending order) Write a program that reads four integer numbers and
checks whether the numbers are all positive and entered in ascending order or
not. The program displays a message indicating whether the numbers are in
ascending order or not based on the order of entered numbers'''

# Prompt the user to enter numbers
num1 = int(input("Please enter number 1: "))
num2 = int(input("Please enter number 2: "))
num3 = int(input("Please enter number 3: "))
num4 = int(input("Please enter number 4: "))

status = "positive"
# Check numbers are negative or not
if num1 < 0 and num2 < 0 and num3 < 0 and num4 < 0:
    status = "negative"
if num1 < 0 or num2 < 0 or num3 < 0 or num4 < 0:
    status = "some negative"

# Check numbers in ascending order
if num1 < num2 and num2 < num3 and num3 < num4:
    print("The numbers are", status,"and entered in ascending order")
else:
    print("The numbers are", status, "and not entered in ascending order")