# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Science: wind-chill temperature) Programming Exercise 2.9 gives a formula
to compute the wind-chill temperature. The formula is valid for temperatures in
the range between −58ºF and 41ºF and wind speed greater than or equal to 2.
Write a program that prompts the user to enter a temperature and a wind speed.
The program displays the wind-chill temperature if the input is valid; otherwise,
it displays a message indicating whether the temperature and/or wind speed is
invalid.'''

import math
#Promt the user for input
t = float(input("Enter the temperature in Fahrenheit: "))
v = float(input("Enter the wind speed miles per hour: "))

if t <= -58 or t >= 41 or v <= 2:
    print("The temperature and/or wind speed is invalid")
else:
    wci = (35.74 + 0.6215*t -  35.75*math.pow(v, 0.16) + 0.4275*t*math.pow(v, 0.16)) # Compute wind chill index
    print("The wind chill index is ", wci) #Display results


