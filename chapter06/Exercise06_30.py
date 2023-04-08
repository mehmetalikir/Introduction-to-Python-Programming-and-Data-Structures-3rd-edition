# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: chance of winning at craps) Revise Exercise 6.28 to run it 10,000 times
and display the number of winning games.'''

import random


def randomDice():
    # Sum of the two random dice
    dice = random.randint(1, 6)

    return dice


def crapsGame():
    # Assign values
    casino = 0
    you = 0

    # Run it 10_000 times
    for i in range(0, 10_000, +1):
        # Assign values
        dice1 = randomDice()
        dice2 = randomDice()
        sum = dice1 + dice2

        # If the sum is 2, 3, or 12 (called craps), you lose
        if sum == 2 or sum == 3 or sum == 12:
            print(f"You rolled {dice1} + {dice2} = {sum}")
            print("Craps! Sorry, you lose.")
            casino += 1

        # If the sum is 7 or 11 (called natural), you win
        elif sum == 7 or sum == 11:
            print(f"You rolled {dice1} + {dice2} = {sum}")
            print("Natural! Congratulations, you win.")
            you += 1

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
                    casino += 1
                    break

                # Otherwise(point is rolled), you win
                elif newSum == sum:
                    print(f"You rolled {dice1} + {dice2} = {newSum}")
                    print("Congratulations, you win.")
                    you += 1
                    break

                # Continue to roll the dice until either a 7 or the same point value is rolled
                else:
                    print(f"You rolled {dice1} + {dice2} = {newSum}")
                    continue

    # Display the number of winning games
    print("--------------------------")
    print(f"Casino win {casino} times")
    print(f"You win {you} times")


def main():
    crapsGame() # Invoke function


main()
