# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Sum a series) Write a program to sum the following series:
1 / 3 + 3 / 5 + 5 / 7 + 7 / 9 + 9 / 11 + 11 / 13 + ... + 95 / 97 + 97 / 99'''

# Assign values
n = 1
sum = 0

# Sum the series
while n <= 97:
    sum += n / n + 2
    n += 2

# Display result
print("Sum: ", sum)

