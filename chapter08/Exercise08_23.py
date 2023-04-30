# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: find the flipped cell) Suppose you are given a 6 x 6 matrix filled
with 0s and 1s. All rows and all columns have the even number of 1s. Let the
user flip one cell (i.e., flip from 1 to 0 or from 0 to 1) and write a program to
find which cell was flipped. Your program should prompt the user to enter a
6 x 6 two-dimensional list with 0s and 1s and find the first row r and first
column c where the even number of 1s property is violated. The flipped cell
is at (r, c).'''

import random


def main():
    # Create a list
    grid = createList()

    if isEvenParity(grid):
        print("All rows and columns are even")
        print("-----------------------------")
        flippedGrid = readAGrid()
        LocateFlippedCell(grid, flippedGrid)
    else:
        print("Not all rows and columns are even")


def createList():
    # Initialize matrix
    grid = [[1, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 0],
            [1, 0, 0, 1, 0, 0]]

    return grid


def isEvenParity(grid):
    for i in range(len(grid)):
        sum = 0
        for j in range(len(grid[i])):
            sum += grid[i][j]
        if sum % 2 != 0:
            return False

    for j in range(len(grid[0])):
        sum = 0
        for i in range(len(grid)):
            sum += grid[i][j]
        if sum % 2 != 0:
            return False

    return True


def LocateFlippedCell(grid, flippedGrid):
    # Assign values
    indexRow = 0
    indexCol = 0

    # Locate where the even number of 1s property is violated
    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            if grid[i][j] != flippedGrid[i][j]:
                indexRow = i
                indexCol = j
                break

    print(f"The first row and column where the parity violated is at ({indexRow},{indexCol})")


# Read a 6 x 6 two-dimensional list with 0s and 1s
def readAGrid():
    # 1 1 1 1 0 0
    # 1 0 0 0 0 1
    # 1 0 0 0 1 0
    # 0 0 0 1 1 1
    # 0 1 1 1 1 0
    # 1 0 0 1 0 0
    print("PLease enter a 6 x 6 matrix:")
    grid = []
    for i in range(6):
        line = input().split()
        grid.append([int(x) for x in line])
    return grid


main()  # Invoke main function
