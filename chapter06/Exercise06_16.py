# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Number of days in a year) Write a function that returns the number of days in a
year using the following header:

def numberOfDaysInAYear(year):

Write a test program that displays the number of days in year from 2010 to 2020.'''


# Check if the year is a leap year
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# Function that returns the number of days in specific year
def numberOfDaysInAYear(year):
    if isLeapYear(year):
        return 366
    else:
        return 355


def main():
    # Display result
    for i in range(2010, 2021, +1):
        print("The number of days in year", i, " -> ", numberOfDaysInAYear(i))


main()
