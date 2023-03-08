# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_25
'''(Sum the digits in an integer) Write a program that reads an integer between 0 and
1000 and adds all the digits in the integer. For example, if an integer is 932, the
sum of all its digits is 14.
Hint: Use the % operator to extract digits, and use the // operator to remove the
extracted digit. For instance, 932 % 10 = 2 and 932 // 10 = 93'''

# Prompt the user for input
number = int(input("Please enter an integer between 0 and 1000: "))

# Sum of all its digits
ones = number % 10
number // 10
tens =  number % 10
number // 10
hundreds = number % 10
sum = ones + tens + hundreds

# Display result
print("The sum of all digits in", number, "is", sum)

