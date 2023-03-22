# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the factors of an integer) Write a program that reads an integer and displays
all its smallest factors in increasing order. For example, if the input integer is
120, the output should be as follows: 2, 2, 2, 3, 5.'''

# Read an integer
num = int(input("Please enter a positive integer: "))

divider = 2  # Numbers to test as factors

# Find the factors of an integer
while num // divider != 1:
    if num % divider == 0:
        print(divider, end=",")
        num /= divider
    else:
        divider += 1

# The output
print(num, end=".")

