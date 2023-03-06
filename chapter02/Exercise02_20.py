# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_01
''' (Financial application: calculate interest) If you know the balance and
the annual percentage interest rate, you can compute the interest on the next monthly
payment using the following formula:
interest = balance x (annualInterestRate / 1200)
Write a program that reads the balance and the annual percentage interest rate
 and then displays the interest for the next month. Keep two digits after the decimal point.'''

# Prompt the user for inputs
balance = float(input("Please enter balance: "))  #1000.0
annualInterestRate = float(input("Please enter annual interest rate: ")) #3.5

# Compute the interest on the next monthly payment
interest = balance * (annualInterestRate / 1200)

#Display future investment value with two digits after decimal point
print("The Interest is ", format(interest, ".2f"))



