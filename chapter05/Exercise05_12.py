# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find numbers divisible by 11 and 17) Write a program that displays, five numbers
per line, all the numbers from 1000 to 50000 that are divisible by 11 and 17.
The numbers are separated by exactly one tab.'''

# Constant
PER_LINE = 5

# Assign variable for per line
count = 0

# Display numbers from 1000 to 50000 that are divisible by 11 and 17
for i in range(1000, 50000):
    if i % (11 * 17) == 0:
        print(" ", i)
        count += 1
        if count % PER_LINE == 0:
            count = 0
            print("")
