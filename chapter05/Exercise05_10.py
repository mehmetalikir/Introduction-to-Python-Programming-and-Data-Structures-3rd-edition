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
highestName = 0
highestPrice = 1000


for i in range(numberOfAirlines):
    airlineName = (input("Please enter an airline name: "))
    ticketPrice = int(input("Please enter ticket price: "))
    if ticketPrice < highestPrice:
        highestName = airlineName
        highestPrice = ticketPrice

print(f"Cheapest airline {highestName}'s ticket price is {highestPrice}")