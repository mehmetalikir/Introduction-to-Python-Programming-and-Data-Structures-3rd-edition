# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

# Exercise02_24
'''(Cost of driving) Write a program that prompts the user to enter the distance to
drive, the fuel efficiency of the car in miles per gallon, and the price per gallon,
and displays the cost of the trip.'''

# Prompt the user for inputs
distance = float(input("Enter the driving distance: "))
milesPerGallon = float(input("Enter miles per gallon: "))
pricePerGallon = float(input("Enter price per gallon: "))

# Compute the cost of driving
costOfDriving = (distance / milesPerGallon) * pricePerGallon

# Display result
print("The cost of driving is $", costOfDriving)
