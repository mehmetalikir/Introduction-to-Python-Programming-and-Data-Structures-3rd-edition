# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Financial application: monetary units) Modify Listing 2.5, ComputeChange.py,
to display the nonzero denominations only, using singular words for single
units such as 1 dollar and 1 penny, and plural words for more than one unit such
as 2 dollars and 3 pennies.'''

#Receive the amount
amount  = float(input("Enter an amount , e.g., 11.56: "))

#Covert the amount to cents
remainingAmount = int(amount * 100)

#Find the number of one dollars
numberOfOneDollars =  remainingAmount // 100
remainingAmount =  remainingAmount % 100

#Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

#Find the number of dimes in  the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

#Find the number of nickels in  the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

#Find the number of pennies in  the remaining amount
numberOfPennies = remainingAmount

#Display results
print("Your amount", amount, "consists of")
print(numberOfOneDollars, "dollar") if numberOfOneDollars == 1 else print(numberOfOneDollars, "dollars")
print(numberOfQuarters, "quarter") if numberOfQuarters == 1 else print(numberOfQuarters,"quarters")
print(numberOfDimes, "dime") if numberOfDimes == 1 else print(numberOfDimes,"dimes")
print(numberOfNickels, "nickel") if numberOfNickels == 1 else print(numberOfNickels,"nickels")
print(numberOfPennies, "pennie") if numberOfPennies == 1 else print(numberOfPennies,"pennies")