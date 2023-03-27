# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir
# git config --bool core.bare true

'''(Simulation: heads or tails) Write a program that simulates flipping a coin one
million times and displays the number of heads and tails.'''
import random

# Assign values
heads = 0
tails = 0

# Simulate flipping a coin one billion times
for i in range(0, 1_000_000_000, +1):
    randomNumber = random.randint(0,1)  # Represent values

    if randomNumber == 0:
        heads += 1
    elif randomNumber == 1:
        tails += 1
    else:
        print("Error")

# Display result
print("Heads: ", heads)
print("Tails: ", tails)