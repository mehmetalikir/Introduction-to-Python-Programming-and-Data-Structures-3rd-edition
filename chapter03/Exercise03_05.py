# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find future month) Write a program that prompts the user to enter an integer
for the current month(January is 0, February is 1, ..., and December is 11). Also
prompt the user to enter the number of months elapsed from the current month
and display the future month of the year'''

# Prompt the user for input
currentMonth = int(input("Please enter current month: "))
elapsedMonths = int(input("Please enter the number of months elapsed since current month: "))

# Calculate future month
futureMonth = (currentMonth + elapsedMonths)

# Display result
match currentMonth:
    case 0:
        currentMonth = "January"
    case 1:
        currentMonth = "February"
    case 2:
        currentMonth = "March"
    case 3:
        currentMonth = "April"
    case 4:
        currentMonth = "May"
    case 5:
        currentMonth = "June"
    case 6:
        currentMonth = "July"
    case 7:
        currentMonth = "August"
    case 8:
        currentMonth = "September"
    case 9:
        currentMonth = "October"
    case 10:
        currentMonth = "November"
    case 11:
        currentMonth = "December"

match futureMonth:
    case 0:
        futureMonth = "January"
    case 1:
        futureMonth = "February"
    case 2:
        futureMonth = "March"
    case 3:
        futureMonth = "April"
    case 4:
        futureMonth = "May"
    case 5:
        futureMonth = "June"
    case 6:
        futureMonth = "July"
    case 7:
        futureMonth = "August"
    case 8:
        futureMonth = "September"
    case 9:
        futureMonth = "October"
    case 10:
        futureMonth = "November"
    case 11:
        futureMonth = "December"

print("Current month is", currentMonth, "and the future month is", futureMonth)