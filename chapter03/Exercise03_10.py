# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: multiplication quiz) Listing 3.3, SubtractionQuiz.py, randomly generates a
subtraction question. Revise the program to randomly generate an addition question
with two integers less than 100.'''

import random

# 1. Generate two random single-digit integers
number1 = random.randint(0,9)
number2 = random.randint(0,9)

# 2. If number1 < number2, swap number1 with number2
if number1 < number2:
    number1, number2 = number2, number1 # Simultaneous assigment *

# 3. Prompt the user to answer "What is number1 - number2?"
answer = int(input("What is " + str(number1) + " - " + str(number2) + "? "))

# 4. Grade the answer and display the result
if number1 - number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.")
    print(number1, "-", number2, "is", number1 - number2)