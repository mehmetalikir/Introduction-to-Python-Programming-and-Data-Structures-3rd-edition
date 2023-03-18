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
if b > a:
    b, a = a, b # Simultaneous assignment
if c > b:
    c, b = b, c
if b > a:
    b, a = a, b

print("The sorted numbers in decreasing order are", a, b, c)
# for increasing order a < b < c , a < c < b , b < a < c, b < c < a, c < a < b, c < b < a


a, b, c, d = 2, 9, 7, 14
# Sort 4 integer numbers in ascending order
if b < a:
    b, a = a, b # Simultaneous assignment
if c < b:
    c, b = b, c
if b < a:
    b, a = a, b
if d < c:
    d, c = c, d
if c < b:
    c, b = b, c
if b < a:
    b, a = a, b
print(a, b, c, d)

