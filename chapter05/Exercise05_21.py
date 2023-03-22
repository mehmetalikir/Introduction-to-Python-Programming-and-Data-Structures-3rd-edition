# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display numbers in a pyramid pattern) Write a nested for loop that prints the
following output:'''

import math

# Constant
NUM = 10

for i in range(1,NUM):
    for j in range(0, NUM-i, 1):
        print(end="  ")
    for j in range(1, i+1, 1):
        print("3%d"%(j +1), end="")
    for j in range(i-1, 0, -1):
        print("3%d"%(j -1), end="")
    print('')
