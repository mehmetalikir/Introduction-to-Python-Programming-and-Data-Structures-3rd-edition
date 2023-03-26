# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the cheapest airline ticket) Write a program that prompts the user to enter
the number of airlines and each airline's name and ticket price. Find the airline
with the cheapest ticket and display its name and price. Assume that the number
of airlines is at least 1.'''

# Prompts prompts the user to enter the number of airlines
numberOfAirlines = int(input("Please enter the number of airlines: "))

# Initialize variables
lowestName = 0
lowestPrice = 1000


for i in range(numberOfAirlines):
    airlineName = (input("Please enter an airline name: "))
    ticketPrice = float(input("Please enter ticket price: "))
    if ticketPrice < lowestPrice:
        lowestName = airlineName
        lowestPrice = ticketPrice

print(f"Cheapest airline {lowestName}'s ticket price is {lowestPrice}")