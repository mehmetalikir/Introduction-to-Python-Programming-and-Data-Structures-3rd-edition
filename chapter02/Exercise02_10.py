# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#(Physics: find acceleration)
#Exercise02_10
"""

A sports car accelerates uniformly from an initial speed u
to a final speed v over a distance s.
Find the acceleration a of the car using the following formula:
a = (v² - u²)/2s
Write a program that prompts the user to enter the initial final speed
in meters/second (m/s) and the distance covered.
The program displays the acceleration of the car in m/s²
"""
#Enter the initial speed of car in m/s:
u = float(input("Enter the initial speed of car in m/s:\t"))

#Enter the final speed of car in m/s:
v = float(input("Enter the final speed of car in m/s:\t"))

#Enter the distance covered by car in meters:
s = float(input("Enter the distance covered by car in meters:\t"))

#The acceleration m/s² is:
a = ((v ** 2) - (u ** 2)) / (2 * s)

print("The acceleration is:", a, "m/s²")
