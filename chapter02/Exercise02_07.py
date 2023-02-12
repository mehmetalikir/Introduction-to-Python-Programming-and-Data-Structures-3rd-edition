# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_07
''' (Find the number of years and days) Write a program that prompts the user to
enter the minutes (e.g 1 billion) and display the number of years and days for
the minutes. For simplicity, assume a year has 365 days'''

#Prompts the user to enter the minutes
minutes = int(input('Enter the number of minutes : ')) #1_000_000_000

year = 60 * 24 * 365
years = minutes // year
remainingDays = (minutes % year) // (24 * 60)

print(minutes, ' is approximately ', years, ' and ', remainingDays, ' days')