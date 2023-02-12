# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_01
''' (Convert km/h to m/s) Write a program that reads a value in kilometers pe hour
from the console and displays it in meter per second. The general formula for
the conversion is as follows:'''

# 1 km / 1 h = 1000 m / 3600 s

#Enter sped in km/h
km_h = int(input("Enter sped in km/h : "))
result = km_h * (1000 / 3600)
print(km_h, ' is equal to ', result )



