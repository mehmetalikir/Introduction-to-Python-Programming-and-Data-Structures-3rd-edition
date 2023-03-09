# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the number of days in a month) Write a program that prompts the user
to enter the month and year and displays the number of days in the month. For
example, if the user entered month 2 and year 2000, the program should display
that February 2000 has 29 days. If the user entered month 3 and year 2005, the
program should display that March 2055 had 31 days.'''

# Prompt the user for input
month = int(input("Please enter a month in the year (e.g., 1 for Jan): "))
year = int(input("Please enter a year: "))

# Display result
match month:
    case 1:
        print("January ", year, " has 31 days")
    case 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("February ", year, " has 29 days")
        else:
            print("February ", year, " has 28 days")
    case 3:
        print("March ", year, " has 31 days")
    case 4:
        print("April ", year, " has 30 days")
    case 5:
        print("May ", year, " has 31 days")
    case 6:
        print("June ", year, " has 30 days")
    case 7:
        print("July ", year, " has 31 days")
    case 8:
        print("August ", year, " has 31 days")
    case 9:
        print("September ", year, " has 30 days")
    case 10:
        print("October ", year, " has 31 days")
    case 11:
        print("November ", year, " has 30 days")
    case 12:
        print("December ", year, " has 31 days")
