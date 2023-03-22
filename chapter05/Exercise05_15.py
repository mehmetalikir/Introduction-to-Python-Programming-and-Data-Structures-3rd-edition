# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the largest integer n such that n^3 > 12000) Use a while loop to find the largest
integer n such that n^3 is less than 12000'''

# Assign variable
n = 0

# Find the largest integer n such that n^3 > 12000 and display result
while n * n * n < 12000:
    n += 1
print("n:", n)

