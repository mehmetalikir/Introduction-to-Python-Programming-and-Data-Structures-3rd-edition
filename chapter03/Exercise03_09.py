# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Travel app: fastest route) Suppose you are planning to commute with an option
of two trains. Write a program to find the train with the fastest route that takes minimum
time. The program prompts the user to enter the route length and average
speed of each train and then displays the one with the fastest route.'''

# formula : time = distance / speed

# Prompt the user for input
lenght1 = float(input("Please enter lenght (kms) of the route 1: "))
speed1 = float(input("Please enter speed (km/h) of the train 1: "))
lenght2 = float(input("Please enter lenght (kms) of the route 2: "))
speed2 = float(input("Please enter speed (km/h) of the train 2: "))

# Calculate time using the formula
time1 = lenght1 / speed1
time2 = lenght2 / speed2

# Compare the times and display result
if time1 < time2:
    print("Train 1 has the fastest route")
else:
    print("Train 2 has the fastest route")
