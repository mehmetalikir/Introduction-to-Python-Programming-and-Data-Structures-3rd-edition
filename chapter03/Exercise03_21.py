# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Science: day of the week) Zeller’s congruence is an algorithm developed by
Christian Zeller to calculate the day of the week. The formula is '''

year = int(input("Please enter year: (e.g., 2008): "))
month = int(input("Please enter month: 1-12: "))
dayOfMonth = int(input("Please enter the day of the month: 1-31: "))

# January and February are counted as 13 and 14 in the formula
if month == 1:
    month = 13
    year = year - 1
if month == 2:
    month = 14
    year = year - 1

# Calculate the day of the week
dayOfWeek = (dayOfMonth + (26 * (month + 1)) // 10 + (year % 100)
             + (year % 100) // 4 + (year // 100) // 4 + 5 * (year // 100)) % 7

# Display result
str = ""
match dayOfWeek:
    case 0: str = "Saturday"
    case 1: str = "Sunday"
    case 2: str = "Monday"
    case 3: str = "Tuesday"
    case 4: str = "Wednesday"
    case 5: str = "Thursday"
    case 6: str = "Friday"

print("Day of the week is",str)