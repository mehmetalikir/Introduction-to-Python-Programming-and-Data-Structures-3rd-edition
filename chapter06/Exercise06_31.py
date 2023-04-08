# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Current date and time) Invoking time.time() returns the
elapsed time in seconds since midnight of January 1, 1970. Write a program
that displays the date and time.'''

import time


# Get the time
def showCurrentTime():
    # Constant
    OFFSET = 10  # AU

    currentTime = time.time()  # Get current time

    # Obtain the total seconds since midnight, Jan 1, 1970
    totalSeconds = int(currentTime)

    # Get the current second
    currentSecond = totalSeconds % 60

    # Obtain the total minutes
    totalMinutes = totalSeconds // 60

    # Compute the current minute in the hour
    currentMinute = totalMinutes % 60

    # Obtain the total hours
    totalHours = totalMinutes // 60

    # Compute the current hour
    currentHour = (totalHours + OFFSET) % 24

    #  Obtain the total days
    totalDays = totalHours // 24

    #  Get current date
    currentDate = getDate(totalDays)

    # Display result
    print("Current date and time is", currentDate, currentHour,
          ":", currentMinute, ":", currentSecond, "GMT")


# Get the date
def getDate(days):
    # Assign values
    year = 1970
    month = 1
    day = 1
    monthdays = getNumberOfDaysInMonth(year, month)  # Obtain number of days in the month
    for i in range(0, days, +1):
        day += 1
        # Increase month and reset day after 28, 29, 30 or 31
        if day > monthdays:
            month += 1
            day = 1
        # Increase year and reset month after 12
        if month > 12:
            year += 1
            month = 1

        monthdays = getNumberOfDaysInMonth(year, month)

    return getMonthName(month), day, year


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


def main():
    showCurrentTime() # Invoke function


main()  # Call the main function
