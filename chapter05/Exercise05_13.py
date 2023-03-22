# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find numbers divisible by 11 or 17, but not both) Write a program that displays, five numbers
pers line, all the numbers from 1000 to 1100 that are divisible by 11 or 17, but not both.
The numbers are separated by exactly one tab.'''

# Constant
PER_LINE = 5

# Assign variable for per line
count = 0

# Display numbers from 1000 to 50000 that are divisible by 11 or 17, but not both.
for i in range(1000, 1100):
    if i % 11 == 0 or i % 17 == 0:
        print(" ", i)
        count += 1
        if count % PER_LINE == 0:
            count = 0
            print("")
