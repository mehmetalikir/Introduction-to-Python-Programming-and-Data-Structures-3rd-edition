# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Use trigonometric functions) Print the following table to display the cos value
and tan value of degrees from 0 to 360 with increments of 20 degrees. Round
the value to keep four digits after the decimal point'''

import math

degree = 0 # Initialize variable

# Display header for table
print("Degree     Cos      Tan")

# Display table
while degree <= 360:
    print(degree, "     ", round(math.cos(math.radians(degree)), 4), "      ", round(math.tan(math.radians(degree)), 4))
    degree += 20
