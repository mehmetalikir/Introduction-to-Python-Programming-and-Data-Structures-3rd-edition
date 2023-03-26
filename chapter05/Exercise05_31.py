
# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display calendars) Write a program that prompts the user to enter the year and
first day of the year and displays the calendar table for the year on the console. For
example, if the user entered the year 2013, and 2 for Tuesday, January 1, 2013,
your program should display the calendar for each month in the year, as follows: '''

# Prompt the user to enter year
year = int(input("Please enter a year: "))

# Prompt the user to enter first day of year
day = int(input("Please enter the first day of the year: "))

# Check if leap year
if year % 4 != 0 and year % 400 != 0:
    febDays = 28
else:
    febDays = 29

# Calculate month, day and output to console
i = 1
while i <= 12:
    match i:
        case 1:
            monthName = "January"
            monthDays = 31
        case 2:
            monthName = "February"
            monthDays = febDays
        case 3:
            monthName = "March"
            monthDays = 31
        case 4:
            monthName = "April"
            monthDays = 30
        case 5:
            monthName = "May"
            monthDays = 31
        case 6:
            monthName = "June"
            monthDays = 30
        case 7:
            monthName = "July"
            monthDays = 31
        case 8:
            monthName = "August"
            monthDays = 31
        case 9:
            monthName = "September"
            monthDays = 30
        case 10:
            monthName = "October"
            monthDays = 31
        case 11:
            monthName = "November"
            monthDays = 30
        case 12:
            monthName = "December"
            monthDays = 31
    match day:
        case 0:
            dayName = "Sunday"
        case 1:
            dayName = "Monday"
        case 2:
            dayName = "Tuesday"
        case 3:
            dayName = "Wednesday"
        case 4:
            dayName = "Thursday"
        case 5:
            dayName = "Friday"
        case 6:
            dayName = "Saturday"
    i += 1

    # Display output
    print("-----------------------------")
    print(" Sun Mon Tue Wed Thu Fri Sat")

    for i in range(1, monthDays + 1, +1):

        if i < 10:
            print(" ",i, end=" ")
        else:
            print(" ",i, end=" ")

        if (i + day) % 7 == 0:
            print()
    print(end="")
    startDay = (day + monthDays) % 7
