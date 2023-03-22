# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the largest integer n such that n3 - n2 < 1,000) Use a while loop to find the
first integer n such that n3 - n2 does not exceed 1000'''

# Assign variable for loop
n = 0

# Find the largest n such that n3 - n2 < 1,000 and display result
while n >= 0:
    if (n * n * n) - (n * n) > 1000:
        print("n : ", n - 1)
        break
    n += 1
