# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display the first days of each month) Write a program that prompts the user to
enter the year and first day of the year, and displays the first day of each month
in the year on the console. For example, in the following sample run, the user
entered year 2013, and 2 for Tuesday, January 1, 2013'''

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
    print(monthName, " 1, ", year, " : ", dayName)
    day = (day + monthDays) % 7
