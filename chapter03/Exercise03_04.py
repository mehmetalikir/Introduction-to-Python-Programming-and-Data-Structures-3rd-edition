# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: multiply two numbers) The program in Listing 3.1 generates two integers
and prompts the user to enter the sum of these two integers. Revise the program
to generate two two-digit nonzero integers and prompt the user to enter the
product of these two integers'''

import random

# Generate random numbers
number1 = random.randint(10,100)
number2 = random.randint(10,100)

# Prompt the user to enter an answer
answer = eval(input("What is " + str(number1) + " * " + str(number2) + "? "))

# Display result
print(number1, "*", number2, "=", answer, "is", number1 * number2 == answer)