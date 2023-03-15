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


num1, num2, num3, num4 = 2, 9, 7, 14
# Sort 4 integer numbers in ascending order
if num2 < num1:
    num2, num1 = num1, num2 # Simultaneous assignment
if num3 < num2:
    num3, num2 = num2, num3
if num2 < num1:
    num2, num1 = num1, num2
if num4 < num3:
    num4, num3 = num3, num4
if num3 < num2:
    num3, num2 = num2, num3
if num2 < num1:
    num2, num1 = num1, num2
print(num1,num2,num3,num4)

