# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Financial application: compare loans with various interest rates) Write a program
that lets the user enter the loan amount and loan period in numbers of years
and displays the monthly and total payments for each interest rate starting from
5% to 8%, with an increment of 1/8. Here is a sample run:'''
import math

# Constant
ANNUAL_INTEREST_RATE = 5

# Prompt the user enter the loan amount and loan period in numbers of years
amount = float(input("Please enter loan amount, for example 120000.95: "))
years = float(input("Please enter number of years as an integer, for example 5: "))

# Format header
print("%-1s%20s%20s\n" % ("Interest Rate", "Monthly Payment", "Total Payment"))

# Display different interest rates
while ANNUAL_INTEREST_RATE <= 8:

    # Calculating monthly and total payment rates
    monthlyInterestRate =  ANNUAL_INTEREST_RATE / 1200
    monthlyPayment = amount * monthlyInterestRate / (1 - 1 / math.pow(1 + monthlyInterestRate, years * 12))

    totalPayment = monthlyPayment * years * 12


    # Display result
    print("%-1.3f%s%17.2f%24.2f \n" % (ANNUAL_INTEREST_RATE,"%", monthlyPayment, totalPayment))
    ANNUAL_INTEREST_RATE += 0.125