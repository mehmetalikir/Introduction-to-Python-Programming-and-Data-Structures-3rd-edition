# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_21
''' (Financial application: compound value) Suppose you save $100 each month
into a saving account with annual interest rate of 5%. Therefore, the monthly
interest rate is 0.05/12 = 0.00417. After the first month, the value in the
account becomes
100 * (1 + 0.00417) = 100.417
After the second month, the value in the account becomes
(100 + 100.417) * (1 + 0.00417) = 20.252
After the third month, the value in the account becomes
(100 + 201.252) * (1 + 0.00417) = 302.507
and so on.
    Write a program that prompts the user to enter a monthly saving amount
and displays the account after the sixth month. Keep two digits after the
decimal points.'''

# Declare constant value
MONTHLY_INTEREST_RATE = (1 + 0.00417)

# Prompt the user for input
monthlySaving  = float(input("Please enter monthly saving amount: ")) #100

# Compute the interest on the next monthly payment
currentAccount = 0
currentAccount = monthlySaving * MONTHLY_INTEREST_RATE
currentAccount = (currentAccount + monthlySaving) * MONTHLY_INTEREST_RATE
currentAccount = (currentAccount + monthlySaving) * MONTHLY_INTEREST_RATE
currentAccount = (currentAccount + monthlySaving) * MONTHLY_INTEREST_RATE
currentAccount = (currentAccount + monthlySaving) * MONTHLY_INTEREST_RATE
currentAccount = (currentAccount + monthlySaving) * MONTHLY_INTEREST_RATE

#Display the account value after the sixth month with two digits after decimal point
print("After the sixth month, the account value is " ,format(currentAccount, ".2f"))