# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Perfect number) A positive integer is called a perfect number if it is equal to
the sum of all of its positive divisors, excluding itself. For example, 6 is the first
perfect number because 6 = 3 + 2 + 1. The next is 28 = 14 + 7 + 4 + 2
+ 1. There are four perfect numbers less than 10,000. Write a program to find all
these four numbers.'''

# Find all perfect numbers less than 10,000
for i in range(6, 10001, +1):
    sum = 0
    for j in range(1, i // 2 + 1, +1):
        if i % j == 0:
            sum += j
    if sum == i:
        print("Perfect number : ", i) # Display result

