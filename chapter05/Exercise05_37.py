# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Summation) Write a program to compute the following summation.
1 / 1 + 2√2 + 1 / 2√2 + 2√3 + 1 / 2√3 + 2√4 + ... + 1 / 2√624 + 2√625'''

import math

# Assign value
sum = 0

# Compute summation
for i in range(1, 625, +1):
    sum += 1 / (math.sqrt(i) + math.sqrt(i + 1))

# Display result
print("Summation: ", sum)
