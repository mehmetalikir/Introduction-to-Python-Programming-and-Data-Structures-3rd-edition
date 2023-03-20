# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Use the math.pow function) Write a program that prints the following table
using the pow function in the math module'''
import math

number = 0 # Initialize variable

# Display header for table
print("Real number    Cube Root")

# Display table
while number <= 48:
    print(number, "            ", round(math.pow(number, 1 / 3), 4))
    number += 4