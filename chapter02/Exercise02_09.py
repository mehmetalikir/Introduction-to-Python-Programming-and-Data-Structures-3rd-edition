# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_09
''' (Science: wind-chill temperature) How cold is it outside? The temperature alone
is not enough to provide the answer. Other factors including wind speed, rela-
tive humidity, and sunshine play important roles in determining coldness outside.
In 2011, the National Weather Service (NWS) implemented the new wind-chill
temperature to measure the coldness using temperature and speed. The for-
mola is given as follows:
    twc = 35.74 + 0.6215ta - 35.75v^1.16 + 0.4275tav0.16
where ta is the outside temperature measured in degrees Fahrenheit and v is the
speed measure in miles per hour. twc is the wind-chill temperature. The formula
cannot be used for wid speeds below 2 mph or for temperatures below -58F
or above 41 F
    Write a pogam that promts the user to enter a temperature beteen -58F
    and 41F a wind speed greater than or equal to 2, and thne display the wind-
    cill temperature.'''
import math
#Promt the user for input
t = float(input("Enter the temperature in Fahrenheit between -58 and 41: 5.5"))
v = float(input("Enter the wind speed miles per hour(must be greater than or""equal to 2): 50.9"))

#Compute wind chill index
wci = 35.74 + 0.6215*t -  35.75*math.pow(v, 0.16) + 0.4275*t*math.pow(v, 0.16)

#Display results
print("The wind chill index is ", wci)