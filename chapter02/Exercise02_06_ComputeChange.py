# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


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
print(" ", numberOfOneDollars, "dollars")
print(" ", numberOfQuarters, "quarters")
print(" ", numberOfDimes, "dimes")
print(" ", numberOfNickels, "nickels")
print(" ", numberOfPennies, "pennies")