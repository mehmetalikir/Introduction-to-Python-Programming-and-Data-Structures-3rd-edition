# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

# Exercise02_22
'''(Population projection) Rewrite Programming Exercise 1.11 to prompt the user
to enter the number of years and displays the population after the number of years.
Use the hint in Programming Exercise 1.11 for this program.'''

# Declare constant value
CURRENT_POPULATIONS = 312032486

# Prompt the user for input
years = int(input("PLease enter the number of years: "))

# Calculate population projection
assumptions = 60 * 24 * 365 *(60 / (13 - 7) ) + (60 / 45)

# Display results
print(years,". Year Total Population:", format((CURRENT_POPULATIONS + assumptions * years), ".2f"))
