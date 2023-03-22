
# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display pyramid) Write a program that prompts the user to enter an integer from
1 to 15 and displays a pyramid, as shown in the following sample run:'''

# Constant
NUM = 7

for i in range(0,NUM):
    j = NUM - 1 - i
    while j > 0:
        print(end = " ")
        j -= 1

    k = i + 1
    while k > 0:
        print(k, end = " ")
        k -= 1

    l = 2
    while l < i + 2:
        print(l, end = " ")
        l += 1
    print(end= " ")

