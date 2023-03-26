# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Compute e) You can approximate e using the following series:
e = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / 4! + ... + 1 / i!
Write a program that displays the e value for i = 10000, 20000, …, and 100000.
(Hint: Since i! = i * (i - 1) * c * 2 * 1, then 1 i! is 1 i(i - 1)! Initialize e and
item to be 1 and keep adding a new item to e. The new item is the previous item
divided by i for i = 2, 3, 4, . . . .)'''

# Assign values
e = 1
number = 1

# Compute e values
for i in range(2, 100000, +1):
    number /= i
    e += number

    # Display result
    if i % 10000 == 0:
        print("i -> ",i, " e : ", e)
