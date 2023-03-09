# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Sort three numbers) Write a program that prompts the user to enter
three numbers and displays them in decreasing order'''


# Prompt the user for input
a = float(input("Please enter number1: "))
b = float(input("Please enter number2: "))
c = float(input("Please enter number3: "))

# Display result after sorting
temp = 0
if b > a or c > a:
    temp = a
    a = b
    b = temp
    if c > a:
        temp = a
        a = c
        c = temp
if c > b:
    temp = b
    b = c
    c = temp

print("The sorted numbers in decreasing order are", a, b, c)


# for increasing order a < b < c , a < c < b , b < a < c, b < c < a, c < a < b, c < b < a

