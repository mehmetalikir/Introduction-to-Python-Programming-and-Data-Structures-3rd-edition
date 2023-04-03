# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Financial application: compute the future investment value) Write a function
that computes future investment value at a given interest rate for a specified
number of years. The future investment is determined using the formula in
Programming Exercise 2.19.

Use the following function header:

def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):

For example, futureInvestmentValue(10000, 0.05/12, 5) returns 12833.59.
    Write a test program that prompts the user to enter the investment amount
and the annual interest rate in percent and prints a table that displays future value
for the years from 1 to 30'''
import math

def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):

    # Compute the future investment  value and return
    return investmentAmount * math.pow(1 + monthlyInterestRate, years * 12)

def main():
    # Prompt the user to enter the investment amount and the annual interest rate in percent
    investmentAmount = float(input("Please enter investment amount, for example 100:"))
    yearlyInterestRate = float(input("Please enter interest rate, for example 5.25:"))
    monthlyInterestRate = yearlyInterestRate / 1200

    # Print header of table
    print("Years            Future Value")
    for i in range(1, 31, +1):
        print(f"%-1d\t\t\t\t%10.2f" % (i, futureInvestmentValue(investmentAmount,monthlyInterestRate, i)))

main()




