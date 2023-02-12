# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_04
''' convert ounces into grams
Write a program that converts ounces into grams. One ounce is 28.35 grams'''
oun = float(input("Enter weight in ounces:\t"))
gr = oun * 28.35
print("{:,.2f} ounce is equal to {:,.2f}".format(oun, gr))
