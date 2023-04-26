# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(The Smallest rows and columns) Write a program that randomly fills in 0s and 1s into
a 5 x 5 matrix, prints the matrix, and finds the rows and columns with the least
1s.
00100
01100
01000
01110
The Smallest row index: 0, 2
The Smallest column index: 4'''

import random

# Constant
N = 5


def main():
    # Create a list
    lst = createList()

    # Display result
    findSmallestRow(lst)
    findSmallestCol(lst)


def createList():
    # Create an empty list
    matrix = []

    # Fill in 0s and 1s into a 5 x 5 matrix randomly
    for i in range(N):
        matrix.append([])  # Add an empty new row
        for j in range(N):
            matrix[i].append(random.randint(0, 1))
            print(matrix[i][j], end=" ")  # Print the matrix

        print()

    return matrix


# Find the rows with the least 1s
def findSmallestRow(matrix):
    # Check rows
    rowSum = sum(matrix[0])
    rowList = [0]
    for i in range(1, N):
        if rowSum > sum(matrix[i]):
            rowSum = sum(matrix[i])
            rowList = [i]
        elif rowSum == sum(matrix[i]):
            rowList.append(i)

    # Display result
    print("The smallest row index: ", end="")
    for i in range(len(rowList) - 1):
        print(rowList[i], end=", ")
    print(rowList[len(rowList) - 1])


# Find the columns with the least 1s
def findSmallestCol(matrix):
    # Check columns
    columnSum = sumColumn(matrix, 0)
    columnList = [0]
    for j in range(1, N):
        if columnSum > sumColumn(matrix, j):
            columnSum = sumColumn(matrix, j)
            columnList = [j]
        elif columnSum == sumColumn(matrix, j):
            columnList.append(j)

    # Display result
    print("The smallest column index: ", end="")
    for i in range(len(columnList) - 1):
        print(columnList[i], end=", ")
    print(columnList[len(columnList) - 1])


# Sum column values
def sumColumn(m, j):
    sum = 0
    for i in range(N):
        sum += m[i][j]
    return sum


main()  # Invoke main function
