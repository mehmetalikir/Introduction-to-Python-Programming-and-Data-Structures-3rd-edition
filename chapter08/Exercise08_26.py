# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Row sorting) Implement the following function to sort the rows in a two-dimensional
list. A new list is returned and the original list is intact.

    def sortRows(m):

Write a test program that prompts the user to enter a 3 x 3 matrix of numbers and
displays a new row-sorted matrix.'''


def main():
    SIZE = 3
    print("Enter a 3 by 3 matrix row by row: ")
    m = []

    for i in range(SIZE):
        line = input().split()
        m.append([float(x) for x in line])

    print("The row-sorted list is ")
    printMatrix(sortRows(m))


def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


def sortRows(m):
    result = []
    for row in m:
        result.append(row)

    for row in result:
        row.sort()

    return result


main()  # Invoke main function
