# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Days of a month) Write a program that prompts the user to enter a year and the
first three letters of a month name (with the first letter in uppercase) and displays
the number of days in the month.'''

# Prompts the user to enter a year
year = int(input("Please enter a year: "))

# Prompts the user to enter first three letters of a month name
month = str(input("Please enter a month (first three letters  with the first letter in uppercase): "))

# Check for leap year
leapYear = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

# Display result
if month == "Jan" or month == "Mar" or \
        month == "May" or month == "Jul" or \
        month == "Aug" or month == "Oct" or month == "Dec":
    print(f"{month} {year} has 31 days")
elif month == "Apr" or month == "Jun" or \
        month == "Sep" or month == "Nov":
    print(f"{month} {year} has 30 days")
elif month == "Feb":
    if leapYear:
        print(f"{month} {year} has 29 days")
    else:
        print(f"{month} {year} has 28 days")
else:
    print("Invalid input")
