# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Compute π) You can approximate π by using the following series:
π = 4(1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11 + ... + (-1)i + 1 / 2i - 1)
Write a program that displays the π value for i = 10000, 20000, …, and
100000.'''

import math

pi = 0
for i in range(1,100001,+1):
    pi += math.pow(-1, i + 1) / (2 * i - 1.0)
    if i == 10000 or i == 20000 or  i == 100000:
        print(f"Pi -> %6d : %.30f" % (i, (pi * 4)))
