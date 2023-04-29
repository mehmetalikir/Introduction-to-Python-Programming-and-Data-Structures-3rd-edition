# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Explore matrix) Write a program that prompts the user to enter the length of a
square matrix, randomly fills in 0s and 1s into the matrix, prints the matrix, and
finds the rows, columns, and major diagonal with all 0s or all 1s.'''
import random


def main():
    # Prompt the user to enter the numbers of matrix
    n = 4  # int(input("Enter the length of a square matrix: "))

    # Create a list of numbers
    a = createList(n)

    # Print the list
    printList(a, n)

    # Find the rows, columns, and major diagonal with all 0s or all 1s and display it
    displayResult(a, n)


def createList(n):
    # Create an empty list
    matrix = []

    # Fill in 0s and 1s into n x n matrix randomly
    for i in range(n):
        matrix.append([])  # Add an empty new row
        for j in range(n):
            matrix[i].append(random.randint(0, 1))

    return matrix


def printList(a, n):
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")  # Print the matrix
        print()


# Display result
def displayResult(a, n):
    for i in range(n):
        for j in range(n):
            if isSameOnARow(a, n):
                print("All ", str(a[i][0]), "'s on row ", i)
            if not isSameOnARow(a, n):
                print("No same numbers on a row")
            if isSameOnAColumn(a, n):
                print("All ", str(a[0][j]), "'s on column ", str(j))
            if not isSameOnAColumn(a, n):
                print("No same numbers on a column")
            if isMajorDiagonal(a, n):
                print("All ", str(a[0][0]), "'s on major diagonal")
            if not isMajorDiagonal(a, n):
                print("No same numbers on the major diagonal")
            if isSubDiagonal(a, n):
                print("All ", str(a[0][n - 1]), "'s on sub-diagonal")
            if not isSubDiagonal(a, n):
                print("No same numbers on the sub-diagonal")
            break
        break


# Check rows
def isSameOnARow(a, n):
    for i in range(n):
        for j in range(1, n):
            if a[i][0] != a[i][j]:  # Check whether row has not same values
                return False
    return True


# Check columns
def isSameOnAColumn(a, n):
    for i in range(n):
        for j in range(1, n):
            if a[0][j] != a[i][j]:  # Check whether column has not same values
                return False
    return True


# Check major diagonal
def isMajorDiagonal(a, n):
    for i in range(1, n):
        if a[0][0] != a[i][i]:  # Check whether major diagonal has not same values
            return False
    return True


# Check sub-diagonal
def isSubDiagonal(a, n):
    for i in range(1, n):
        if a[0][n - 1] != a[i][n - 1 - i]:  # Check whether sub-diagonal has not same values
            return False
    return True


main()  # Invoke main function
