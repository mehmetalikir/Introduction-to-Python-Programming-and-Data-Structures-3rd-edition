# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Pattern recognition: four consecutive equal numbers) Write the following
function that tests whether a two-dimensional list has four consecutive numbers
of the same value, either horizontally, vertically, or diagonally:

    def isConsecutiveFour(values):

Write a test program that prompts the user to enter the number of rows and
columns of a two-dimensional list and then the values in the list. The program
displays True if the list contains four consecutive numbers with the
same value; otherwise, it displays False. Here are some examples of the
True cases:'''
import random

# Constant
N = 4


def main():
    # Prompt the user to enter the numbers of matrix
    n = 10  # int(input("Enter the length of a square matrix: "))

    # Create a list of numbers
    a = createList(n)

    # Print the list
    printList(a, n)

    # Find consecutive fours in the rows, columns, and diagonal
    isConsecutiveFour(a, n)


def createList(n):
    # Create an empty list
    matrix = []

    # Fill in 0s and 1s into n x n matrix randomly
    for i in range(n):
        matrix.append([])  # Add an empty new row
        for j in range(n):
            matrix[i].append(random.randint(0, 9))

    return matrix


def printList(a, n):
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")  # Print the matrix
        print()


# Display result
def isConsecutiveFour(a, n):
    if isSameOnARow(a, n) or \
            isSameOnAColumn(a, n) or \
            isSubDiagonal(a, n) or \
            isMajorDiagonal(a, n):
        return print("True")
    return print("False")


# Check rows
def isSameOnARow(a, n):
    # Assign value
    count = 0
    for i in range(0, len(a) - 1):
        for j in range(1, len(a) - 1):
            if a[i][0] == a[i][j + 1]:  # Check whether row has not same values
                count += 1

    if count == 4:
        return True
    return False


# Check columns
def isSameOnAColumn(a, n):
    # Assign value
    count = 0
    for i in range(len(a) - 1):
        for j in range(1, len(a) - 1):
            if a[0][j] == a[i + 1][j]:  # Check whether column has not same values
                count += 1

    if count == 4:
        return True
    return False


# Check major diagonal
def isMajorDiagonal(a, n):
    # Assign value
    count = 0
    for i in range(1, len(a) - 1):
        if a[0][0] == a[i][i]:  # Check whether major diagonal has not same values
            count += 1

    if count == 4:
        return True
    return False


# Check sub-diagonal
def isSubDiagonal(a, n):
    # Assign value
    count = 0
    for i in range(1, len(a) - 1):
        if a[0][n - 1] == a[i][n - 2]:  # Check whether sub-diagonal has not same values
            count += 1

    if count == 4:
        return True
    return False


main()  # Invoke main function
