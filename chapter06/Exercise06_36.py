# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Compute the probability) Write a function rollDice(n) that randomly
generates a number from 1 to 6 and counts the total occurrences of 6, there times
in row. Test your program for n=1_000_000'''

import random


# Randomly generates a number from 1 to 6
def getRandomNumbers(r):
    return random.randint(0, r)


def rollDice(n):
    # Constant
    ROWS_PER_LINE = 50  # Numbers of rows to display per line

    # Assign value
    count = 0

    # Print random numbers between '0' and '6', 3 rows per line
    for i in range(0, n):
        num = getRandomNumbers(6)
        print(num, end="")
        if num == 6:
            count += 1
        if (i + 1) % ROWS_PER_LINE == 0:
            print()  # Jump to the new line

    print("______________________________________________________")
    print(f"The occurrence of number 6 is {count} in {n} rolled")


def main():
    n = 1_000_000
    rollDice(n)


main()  # Call the main function
