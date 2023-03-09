# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: square of a number) The program in Listing 3.1, generates two integers
and prompts the user to enter the sum of these two integers.
Revise the program to generate one single-digit integer and prompt the user to
enter the square of the integers.'''

import random

# Generate random numbers
number1 = random.randint(0,9)

# Prompt the user to enter an answer
answer = eval(input("What is " + str(number1) + " ^ 2 ? "))

# Display result
print(number1, "^ 2", "=", answer, "is", number1 ** 2 == answer)
