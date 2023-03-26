# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Financial application: compound value) Suppose you save $100 each month
into a savings account with the annual interest rate 5%. So, the monthly interest
rate is 0.05 / 12 = 0.00417. After the first month, the value in the account
becomes
        100 * (1 + 0.00417) = 100.417
After the second month, the value in the account becomes
        (100 + 100.417) * (1 + 0.00417) = 201.252
After the third month, the value in the account becomes
        (100 + 201.252) * (1 + 0.00417) = 302.507
and so on.
Write a program that prompts the user to enter an amount (e.g., 100), the annual
interest rate (e.g., 5), and the number of months (e.g., 6) and displays the amount
in the savings account after the given month.'''

# Prompt the user to enter an amount
savingAmount = float(input("Please enter the amount to be saved for each month: "))

# Prompt the user to enter the annual interest rate
annualInterestRate = float(input("Please enter the annual interest rate: "))

# Prompt the user to enter the number of months
numberOfMonths = int(input("Please enter the number of months: "))

# Compute monthly interest rate
monthlyInterestRate = annualInterestRate / 1200

# Compute amount in the savings account
accountValue = 0
for i in range(1,numberOfMonths+1, +1):
    accountValue = (savingAmount + accountValue) * (1 + monthlyInterestRate)

# Display result
print(f"After the {numberOfMonths}. the account value is %.2f" % (accountValue))