# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Subtraction quiz) Rewrite Listing 5.1, RepeatSubtractionQuiz.py, to alert the
user if an answer is entered again. Hint: Use a list to store answers.'''

import random


def main():
    subtractionQuiz()


# Alert the user if an answer is entered again
def subtractionQuiz():
    # Generate two random single-digit integers
    num1 = getRandomInteger()
    num2 = getRandomInteger()

    # If num1 < num2 swap the numbers
    if num1 < num2:
        num1, num2 = num2, num1

    # Create an empty list
    lst = []

    # Prompt the user to answer
    answer = int(input("What is " + str(num1) + " - " + str(num2) + " ? "))
    lst.append(answer)

    # Repeatedly ask the user the question until it is correct
    while num1 - num2 != answer:
        answer = (int(input("Wrong answer. Try it again. "
                            "What is " + str(num1) + " - " + str(num2) + " ? ")))
        if lst[len(lst) - 1] == answer:
            print(f"You already entered {answer}")
            continue

    print("You got it!")


# Generate random single-digit
def getRandomInteger():
    return random.randint(0, 9)


main()  # Call main function
