# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Random character) Write a program that displays a random lowercase or
uppercase letter'''

import random # Import random module to use the random functions

# Randomize the ASCII value of the lowercase and uppercase
lowercase = random.randint(97,122)
uppercase = random.randint(65,90)

# Display result
print(f"Random letters are {chr(lowercase)} and {chr(uppercase)}")