# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Conversion from gallons to litters) Write a program that displays the following
two tables side by side (note that 1 gallon is 3.785 liters):'''

gallon = 2 # Initialize variable
litter = 10 # Initialize variable

# Display header for table
print("Gallons      Liters  |  Gallons      Liters")

# Display table
while gallon <= 100:
    print(gallon,"          ", format((gallon * 3.785), ".1f" ), "   | ", litter,"          ", format((litter / 3.785), ".2f" ))
    gallon += 2
    litter += 3
