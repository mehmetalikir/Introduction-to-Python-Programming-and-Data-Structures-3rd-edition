# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Print Calendar) Programming Exercise 3.21 uses Zeller’s congruence to calculate
the day of the week. Simplify Listing 6.13, PrintCalendar.py, using Zeller’s
algorithm to get the start day of the month.'''


# Print the calendar for a month in a year
def printMonth(year, month):
    # Print the headings of the calendar
    printMonthTitle(year, month)

    # Print the body of the calendar
    printMonthBody(year, month)


# Print the month title e.g., May, 1999
def printMonthTitle(year, month):
    print("         ", getMonthName(month), " ", year)
    print("------------------------------")
    print(" Sun Mon Tue Wed Fri Sat")


# Print month body
def printMonthBody(year, month):
    # Get start day of week for the first date in the month
    startDay = getStartDay(year, month)

    # Get number of days in month
    numberOfDaysInMonth = getNumberOfDaysInMonth(year, month)

    # Pad space before the first day in the month
    i = 0
    for i in range(startDay):
        print("    ", end="")

    for i in range(1, numberOfDaysInMonth + 1):
        print(f"{i:4d}", end="")

        if (i + startDay) % 7 == 0:
            print()  # Jump to the new line


# Get the English name for the month
def getMonthName(month):
    if month == 1:
        monthName = "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName = "April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month == 7:
        monthName = "July"
    elif month == 8:
        monthName = "August"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    else:
        monthName = "December"

    return monthName


# Get the start day of month/ 1 / year
def getStartDay(year, month):
    if month == 1 or month == 2:
        month = 13 if month == 1 else 14
        year -= 1

    # Implement Zeller's Algorithm
    return (1 + (26 * (month + 1)) // 10 + (year % 100) +
            (year % 100) // 4 + (year // 100) // 4 + 5 *
            (year // 100)) % 7 - 1


# Get the number of days in a month
def getNumberOfDaysInMonth(year, month):
    if (month == 1 or month == 3 or month == 5 or month == 7 or
            month == 8 or month == 10 or month == 12):
        return 31

    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    if month == 2:
        return 29 if isLeapYear(year) else 28

    return 0  # If month is incorrect


# Determine if it is a leap year
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main():
    # Prompt the user to enter year and month
    year = int(input("Please enter full year (e.g, 2001): "))
    month = int(input("Please enter month as number between 1 and 12: "))

    # Print calendar for the month of the year
    printMonth(year, month)


main()  # Call the main function
