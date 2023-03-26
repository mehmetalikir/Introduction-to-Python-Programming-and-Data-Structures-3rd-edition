# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''For the formula to compute monthly payment, see Listing 2.8, ComputeLoan.py.
(Financial application: loan amortization schedule) The monthly payment for a
given loan pays the principal and the interest. The monthly interest is computed
by multiplying the monthly interest rate and the balance (the remaining principal).
The principal paid for the month is therefore the monthly payment minus the
monthly interest. Write a program that lets the user enter the loan amount,
number of years, and interest rate and displays the amortization schedule for the
loan.'''

import math

# Enter loan amount
loanAmount = float(input("Please enter loan amount, for example 120000.95: "))

# Enter number of years
years = int(input("Please enter number of years as an integer, for example 5: "))

# Enter annual interest rate
annualInterestRate = float(input("Please enter yearly interest rate, for example 8.25:  "))

# Obtain monthly interest rate
monthlyInterestRate = annualInterestRate / 1200

# Calculate payment
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 /
                                                     math.pow(1 + monthlyInterestRate, years * 12))

# Display monthly payment
print(f"Monthly Payment: %.2f" % (monthlyPayment))

# Display total payment
print(f"Total Payment: %.1f" % ((monthlyPayment * 12) * years))

# Format header
print(f"%-1s%20s%20s%20s" % ("Payment#", "Interest", "Principal", "Balance"))

# Display result
balance, principal, interest = loanAmount, 0, 0,
for i in range(1, (years * 12)+1, +1):
    interest = monthlyInterestRate * balance
    principal = monthlyPayment - interest
    balance = balance - principal
    print(f"%-1d%24.2f%22.2f%22.2f" % ( i, interest,
          principal, balance))

# print( i, "\t\t", interest, "\t\t",principal, "\t\t", balance)
