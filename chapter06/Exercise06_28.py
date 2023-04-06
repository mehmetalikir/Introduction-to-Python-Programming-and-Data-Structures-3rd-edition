# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: craps) Craps is a popular dice game played in casinos. Write a program
to play a variation of the game, as follows:
Roll two dice. Each die has six faces representing values 1, 2, …, and 6, respectively.
Check the sum of the two dice. If the sum is 2, 3, or 12 (called craps), you
lose; if the sum is 7 or 11 (called natural), you win; if the sum is another value
(i.e., 4, 5, 6, 8, 9, or 10), a point is established. Continue to roll the dice until either
a 7 or the same point value is rolled. If 7 is rolled, you lose. Otherwise, you win.
Your program acts as a single player.'''

import random


def randomDice():
    # Sum of the two random dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    return dice1 + dice2


def main():
    sum = randomDice()  # Assign value

    if sum == 2 or sum == 3 or sum == 12:
        print(f"{[sum]} Craps! Sorry, you lose.")
    elif sum == 7 or sum == 11:
        print(f"{[sum]} Natural! Congratulations, you win.")
    else:
        point = sum
        while True:
            if point == 7:
                print(f"{[point]} Sorry, you lose")
                break
            else:
                print(f"{[point]} Congratulations, you win.")
                break


main()
