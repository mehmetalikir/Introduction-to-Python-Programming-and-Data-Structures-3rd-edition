# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Random number chooser) You can shuffle a list using random.shuffle(lst)
Write your own function without using random.shuffle(lst) to shuffle a list
and return the list. Use the following function header:

    def shuffle(lst):

Write a test program that prompts the user to enter a list of numbers in one line,
invokes the function to shuffle the numbers, and displays the numbers.'''

import random

def main():
    # Create a list of numbers
    lst = createList()

    # Displays the mean and standard deviation
    displayResult(lst)


def createList():
    # Prompt the user to enter list of numbers
    s = input("Please enter numbers: ")  # 1.9 2.5 3.7 2 1.5 6 3 4 5 2.5
    lst = [float(x) for x in s.split(" ")]

    return lst


# Display result
def displayResult(list1):
    print(shuffle(list1))


def shuffle(lst):
    # Create an empty list
    shuffled = []

    for i in range((len(lst))):
        shuffled.append(lst[randomIndex(lst)]) # Invoke function as index

    return shuffled

# Randomize index
def randomIndex(lst):
    return random.randint(0, len(lst) -1)



main()  # Invoke main function

