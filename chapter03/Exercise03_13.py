# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Financial application: compute taxes) Listing 3.6, ComputeTax.py, gives the
source code to compute taxes for single filers. Complete Listing 3.6 to give the complete
the source code for the other filing statuses.'''

import sys

# Prompt the user to enter filing status
status = int(input("Please enter the filing status: "))

# Prompt the user to enter taxable income
income = float(input("Please the taxable income: "))

# Compute tax
tax = 0

if status == 0:  # Compute tax for single filers
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
    elif income <= 171550:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25 + (income - 82250) * 0.28
    elif income <= 372950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25 + (income - 82250) * 0.28 + (income - 171550) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25 + (income - 82250) * 0.28 + (
                    income - 171550) * 0.33 + (income - 372950) * 0.35
elif status == 1: # Compute tax for married file jointly
    print("TODO")
elif status == 2: # Compute tax for married separately
    print("TODO")
elif status == 3: # Compute tax for head of household
    print("TODO")
else:
    print("Please enter valid status")
    sys.exit()
print("Tax is", tax)


