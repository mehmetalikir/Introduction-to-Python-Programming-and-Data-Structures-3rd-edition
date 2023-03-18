# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Order three cities) Write a program that prompts the user to enter there cities
and displays them in ascending order.'''

# Prompts the user to enter there cities
str1 = str(input("Please enter first city: "))
str2 = str(input("Please enter second city: "))
str3 = str(input("Please enter third city: "))

# Swap strings in ascending order
if str2 < str1:
    str2, str1 = str1, str2 # Simultaneous assignment
if str3 < str2:
    str3, str2 = str2, str3
if str2 < str1:
    str2, str1 = str1, str2

# Display result
print(str1, str2, str3)