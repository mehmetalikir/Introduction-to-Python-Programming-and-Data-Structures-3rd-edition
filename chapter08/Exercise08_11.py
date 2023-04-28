# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: nine heads and tails) Nine coins are placed in a 3 x 3 matrix with some
face up and some face down. You can represent the state of the coins with the values
0 (heads) and 1 (tails). Here are some examples:

    0 0 0 1 0 1 1 1 0 1 0 1 1 0 0
    0 1 0 0 0 1 1 0 0 1 1 0 1 1 1
    0 0 0 1 0 0 0 0 1 1 0 0 1 1 0

There are a total of 512 possibilities. So, you can use the decimal numbers 0, 1, 2,
3, ..., and 511 to represent all states of the matrix. Write a program that prompts
the user to enter a number between 0 and 511 and displays the corresponding
3 x 3 matrix with the characters H and T.

    Each state can also be represented using a binary number. For example, the preceding
matrices correspond to the numbers:

    000010000 101001100 110100001 101110100 100111110

In following sample run, the user entered 7, which corresponds to 000000111. Since 0 stands for H and
1 for T, the output is correct.'''
import random


def main():
    getIt()  # Invoke function


def getIt():
    # Create an empty list to store values
    matrix = []

    for i in range(3):
        matrix.append([])
        for j in range(3):
            s = random.randint(0, 511)
            # Prompt the user to enter a number between 0 and 511
            # s = int(input("Please enter a number between 0 and 511: "))
            if s % 2 == 0:
                matrix[i].append('H')
            else:
                matrix[i].append('T')

            s /= 2

    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


main()  # Invoke main function
