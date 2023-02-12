# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir
"""
#Exercise02_06
(Financial application: monetary units)
To fix the possible loss of accuracy when coverting a float value
to an int value. For example, the input 1156 represent 11 dollars and 56 cents.
"""
cent = int(input("In cents, enter the amount of money:\t"))
doll = cent // 100
cnt = cent % 100
print("{} cents is: {} dollars and {} cents".format(cent, doll, cnt))
