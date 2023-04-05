# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Display matrix of characters) Write a function that displays an n-by-n matrix using
the following header:

def printMatrix(n):

Each element is a-z, which is generated randomly. Write a test program that
prompts the user to enter n and displays an n-by-n matrix. Here is a sample run:'''

import random


def printMatrix(n):

    # Nested loops to generate the matrix of characters
    for i in range(0, n, +1):
        for j in range(0, n, +1):
            print(chr(random.randint(ord('a'), ord('z'))), end=" ")  # Convert values
        print("") # Break line


def main():
    # Prompt the user to enter n
    n = int(input("Please enter n: "))

    # Display result
    printMatrix(n)


main()
