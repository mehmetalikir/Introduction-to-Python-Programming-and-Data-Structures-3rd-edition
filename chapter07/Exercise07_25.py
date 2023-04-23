# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: pick four cards) Write a program that picks four cards from a deck of 52
cards and computes their sum. An ace, king, queen, and jack represent 1, 13,
12, and 11, respectively. Your program should display the number of picks that
yields the sum of 24.'''

import random


def main():
    # Assign values
    sum = 0
    picks = 0

    while sum <= 24:
        picks += 1
        # Pick four cards from a deck of 52
        for i in range(0, 4):
            sum += (getRandom() % 13) # Compute their sum


    print(f"Sum is {sum} and number of picks: {picks}")

# Generate random card
def getRandom():
    return random.randint(0, 51)


main()  # Invoke main function
