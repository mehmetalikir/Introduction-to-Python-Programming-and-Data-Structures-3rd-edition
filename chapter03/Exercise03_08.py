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
if a > b and b > c:
    print("The sorted numbers in decreasing order are", a, b, c)
elif a > c and c > b:
    print("The sorted numbers in decreasing order are", a, c, b)
elif b > a and b > c:
    print("The sorted numbers in decreasing order are", b, a, c)
elif b > c and c > a:
    print("The sorted numbers in decreasing order are", b, c, a)
elif c > a and a > b:
    print("The sorted numbers in decreasing order are", c, a, b)
elif c > b and b > a:
    print("The sorted numbers in decreasing order are", c, b, a)
else:
    print("Please input valid values")

# for increasing order a < b < c , a < c < b , b < a < c, b < c < a, c < a < b, c < b < a

