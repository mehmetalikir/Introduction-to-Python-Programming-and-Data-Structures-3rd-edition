# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: heads or tails) Write a program that lets the user guess whether a flipped
coin displays the head or the tail. The program randomly generates an integer 0 or 1,
which represents head or tail. The program prompts the user to enter a guess and
reports whether the guess is correct or incorrect.'''

import random

# Generate random numbers
number = random.randint(0,1)

# Prompt the user to enter a guesss
print("Guess head or tail?")
guess = int(input("Please enter 0 for head and 1 for tail: "))

# Check the number head or tail
if number == 0:
    str = "head"
else:
    str = "tail"

# Display result
if guess == number:
    print("Congratulations, it is a", str)
else:
    print("Sorry, it is a", str)
