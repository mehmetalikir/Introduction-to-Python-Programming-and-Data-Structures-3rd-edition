# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: pick a card) Write a program that simulates picking a card from a deck
of 52 cards. Your program should display the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.'''

import random

# Get random mumbers for rank and suit
rankNum = random.randint(0, 12)
suitNum = random.randint(0, 3)

rankName = ""
suitName = ""

# Get rank name
match rankNum:
    case 0:
        rankName = "Ace"
    case 1:
        rankName = "2"
    case 2:
        rankName = "3"
    case 3:
        rankName = "4"
    case 4:
        rankName = "5"
    case 5:
        rankName = "6"
    case 6:
        rankName = "7"
    case 7:
        rankName = "8"
    case 8:
        rankName = "9"
    case 9:
        rankName = "10"
    case 10:
        rankName = "Jack"
    case 11:
        rankName = "Queen"
    case 12:
        rankName = "King"

# Get suit name
match suitNum:
    case 0:
        suitName = "Clubs"
    case 1:
        suitName = "Diamonds"
    case 2:
        suitName = "Hearts"
    case 3:
        suitName = "Spades"

# Display the lucky card
print("The card you picked is", rankName, "of", suitName)
