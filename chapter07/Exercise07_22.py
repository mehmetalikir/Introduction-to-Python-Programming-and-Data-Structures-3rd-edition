# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Simulation: coupon collector’s problem) Coupon collector is a classic statistics
problem with many practical applications. The problem is to pick objects from
a set of objects repeatedly and find out how many picks are needed for all the
objects to be picked at least once. A variation of the problem is to pick cards from
a shuffled deck of 52 cards repeatedly and find out how many picks are needed
before you see one of each suit. Assume a picked card is placed back in the deck
before picking another. Write a program to simulate the number of picks needed
to get four cards from each suit and display the four cards picked (it is possible a
card may be picked twice)'''

import random


def main():
    # Assign values
    count = 0
    picks = 0

    # Create a list to hold each suit
    suitCount = [0] * 4

    # Simulate the number of picks needed to get four cards from each suit
    while count < 4:
        randomCard = getRandom()
        picks += 1
        if suitCount[randomCard // 13] == 0:
            suitCount[randomCard // 13] += 1
            count += 1

            # Display the four cards picked
            getCard(randomCard)

    print("Number of picks: ", picks)


def getCard(randomCard):
    # Create a deck of cards
    deck = [x for x in range(0, 52)]

    # Create suits and ranks lists
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
             "10", "Jack", "Queen", "King"]

    # Pick random card from deck
    suit = suits[deck[randomCard] // 13]
    rank = ranks[deck[randomCard] % 13]

    print(rank, "of", suit)


def getRandom():
    return random.randint(0, 51)


main()  # Invoke main function

