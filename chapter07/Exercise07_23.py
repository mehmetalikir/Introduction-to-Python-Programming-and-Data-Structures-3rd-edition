# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

''''''

import random


def main():
    picks = 0
    count = 0
    suitCount = [0] * 4

    while count < 4:
        i = getRandom()
        picks += 1
        if suitCount[i // 13] == 0:
            suitCount[i // 13] += 1
            count += 1
            getCard(i)

    print(picks)


def getCard(i):
    deck = [x for x in range(0, 52)]

    # Create suits and ranks lists
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
             "10", "Jack", "Queen", "King"]

    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]

    print(suit, "of", rank)


def getRandom():
    return random.randint(0, 52)


main()
