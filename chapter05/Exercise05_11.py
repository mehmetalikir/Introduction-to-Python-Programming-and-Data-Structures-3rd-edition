# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the two cheapest airline tickets) Write a program that prompts the user to enter
the number of airlines and each airline's name and ticket price and display the name and ticket price of
two airlines with the cheapest tickets. Assume that the number of airlines is at least 2.'''

# Prompts prompts the user to enter the number of airlines
numberOfAirlines = int(input("Please enter the number of airlines: "))

# Initialize variables
lowestName = 0
secondLowestName = 0
lowestPrice = 1000
secondLowestPrice = 1000

for i in range(numberOfAirlines):
    airlineName = (input("Please enter an airline name: "))
    ticketPrice = float(input("Please enter ticket price: "))
    if ticketPrice < lowestPrice:
        secondLowestName = lowestName
        secondLowestPrice = lowestPrice
        lowestName = airlineName
        lowestPrice = ticketPrice

print(f" {lowestName}'s ticket price is {lowestPrice}")

print(f" {secondLowestName}'s ticket price is {secondLowestPrice}")