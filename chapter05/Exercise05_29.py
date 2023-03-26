# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display leap years) Write a program that displays all the leap years, ten per line,
from 101 to 2100, separated by exactly one space. Also display the number of
leap years in this period.'''

# Constant
PER_LINE = 10 * 4

# Assign values
year = 2001
count = 0
totalYear = 0

# Compute the number of leap years in this period
for year in range(year, 2100, +1):
    # Check for leap year
    leapYear = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
    if leapYear:
        totalYear += 1
        print(year, end=" ")
    count += 1
    if count == PER_LINE:  # Display ten years per line
        count = 0
        print()

# Display number of leap years
print("\nNumber of leap years:", totalYear)
