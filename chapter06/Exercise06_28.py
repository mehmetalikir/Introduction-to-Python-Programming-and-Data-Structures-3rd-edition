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
    dice = random.randint(1, 6)

    return dice


def main():
    # Assign values
    dice1 = randomDice()
    dice2 = randomDice()
    sum = dice1 + dice2

    # If the sum is 2, 3, or 12 (called craps), you lose
    if sum == 2 or sum == 3 or sum == 12:
        print(f"You rolled {dice1} + {dice2} = {sum}")
        print("Craps! Sorry, you lose.")

    # If the sum is 7 or 11 (called natural), you win
    elif sum == 7 or sum == 11:
        print(f"You rolled {dice1} + {dice2} = {sum}")
        print("Natural! Congratulations, you win.")

    # If the sum is another value (i.e., 4, 5, 6, 8, 9, or 10), a point is established
    else:
        print(f"You rolled {dice1} + {dice2} = {sum}")
        print(f"point is {sum}")

        # Jump to new rolling and repeat it until 7 or point rolled
        while True:
            # Assign  new values
            dice1 = randomDice()
            dice2 = randomDice()
            newSum = dice1 + dice2

            # If 7 is rolled, you lose
            if newSum == 7:
                print(f"You rolled {dice1} + {dice2} = {newSum}")
                print("Sorry, you lose")
                break

            # Otherwise(point is rolled), you win
            elif newSum == sum:
                print(f"You rolled {dice1} + {dice2} = {newSum}")
                print("Congratulations, you win.")
                break

            # Continue to roll the dice until either a 7 or the same point value is rolled
            else:
                print(f"You rolled {dice1} + {dice2} = {newSum}")
                continue


main()
