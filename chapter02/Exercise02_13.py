# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_10
#(Find the greatest digit)
"""
Write a program that prompts the user to enter a four-
digit integer and displays the greatest digit among
the four digits."""
#Enter a four-digit integer:
digit = input("Enter a four-digit integer:\t")

#Find the greatest digit:
the_greatest_digit = int(max(digit))

print("The greatest digit of",digit, "is:", the_greatest_digit)
