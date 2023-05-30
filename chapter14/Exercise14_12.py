# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Subtraction quiz) Rewrite Programing Exercise 7.36 to store the answer in a
set rather than a list'''

import random

# 1. Generate two random single-digit integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# 2. If number1 < number2, swap number1 with number2
if number1 < number2:
    number1, number2 = number2, number1

# 3. Prompt the student to answer What is number1 - number2?
answer = int(input("What is " + str(number1) + " - "
    + str(number2) + "? "))

s = set()
s.add(answer)

# 5. Repeatedly ask the user the question until it is correct
while number1 - number2 != answer:
    answer = int(input("Wrong answer. Try again. What is "
        + str(number1) + " - " + str(number2) + "? "))
    if (answer in s):
        print("You already entered", answer)
    else:
        s.add(answer)

print("You got it!")
