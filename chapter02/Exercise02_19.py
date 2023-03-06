# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_19
''' (Financial application: calculate future investment value) Write a program that
reads an investment amount, the annual interest rate, and the number of years,
and the display of future investment value using the following formula:
        futureInvestmentValue = investmentAmount x (1 + annualInterestRate) ^ numberOfYears
    For example, if you enter amount 1000, an annual interest rate of 4.25%, and
    the number of years as 1, the future investment value is 1043.33.'''

# Prompt the user for inputs
investmentAmount = float(input("Enter the investment amount, for example 120000.95: ")) # 1000.56
annualInterestRate = float(input("Enter annual interest rate, for example 8.25: ")) # 4.25
numberOfYears = float(input("Enter number of years as an integer, for example 5: ")) # 1

# Calculate future investment value
monthlyInterestRate = annualInterestRate / 1200
futureInvestmentValue =  investmentAmount * (1 + monthlyInterestRate) ** (numberOfYears * 12)

#Display future investment value with two digits after decimal point
print("Future value is ", format(futureInvestmentValue, ".2f"))