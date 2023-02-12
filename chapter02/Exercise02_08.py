# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_08
'''(Science: calculate potential energy) Write a program that calculates the poten-
tial energy needed to take a brick cart from ground to the of a building. The
program should prompt the user to enter the mass of the cart in kilograms and
height of the building in meters. The formula to compute the potential energy is:
Potential Energy = mass * gravity * height
Take gravity  = 9.8 m/s^2
'''

gravity = 9.8
#Promt the user for input
mass = int(input("Enter the mass of cart in kilograms : "))
height = int(input("Enter the height of building in meters : "))

#Compute potential energy
potential_energy = mass * gravity * height

#Display result
print("The potential energy is ", potential_energy, "joules")




