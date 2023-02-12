# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_11
''' (Financial application: investment amount) Suppose you want to deposit a certain
 amount of money into a saving account with a fixed annual interest rate. Write
 a program that prompts the user to enter the final account value, the annual inter-
 est rae in percent, and the number of years, and then displays the initial deposit
 amount. The initial deposit amount can be obtained using the following formula:
    initialDepositAmount = finalAccountValue // (1 + monthlyInterestRate) ** numberOfMonths'''

#Promt the user for input
finalAccountValue = float(input("Enter final account value: 1000 "))
monthlyInterestRate = float(input("Enter annual interest rate in percent, \
for example 8.25: 4.5 ")) / 100 / 12

years = float(input("Enter number of year as an integer,for example 5: 5 "))
numberOfMonths = years * 12

#Compute initial deposit
initialDepositAmount = finalAccountValue / (1 + monthlyInterestRate) ** numberOfMonths
#Display results
print("Initial deposit amount is:",initialDepositAmount)
