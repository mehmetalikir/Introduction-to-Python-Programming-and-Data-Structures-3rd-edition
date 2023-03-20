# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Conversion from gallons to litters) Write a program that displays the following
table (note that 1 gallon is 3.785 liters):'''

gallon = 2 # Initialize variable

# Display header for table
print("Gallons      Liters")

# Display table
while gallon <= 98:
    print(gallon,"          ", format((gallon * 3.785), ".1f" ))
    gallon += 2


