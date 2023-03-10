# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''() Write a program that'''

import random

red = 0
black = 0
for i in range(1_000_000_000):
    number = random.randint(0,1)
    if number == 0:
        red += 1
    else:
        black += 1

print("Red:", red, "Black:", black)


