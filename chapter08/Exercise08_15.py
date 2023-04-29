# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

''''''
import random


def main():
    # Prompt the user to enter the numbers of matrix
    n = 4

    # Create an empty list
    a = []

    # Fill in 0s and 1s into n x n matrix randomly
    for i in range(n):
        a.append([])  # Add an empty new row
        for j in range(n):
            a[i].append(random.randint(0, 1))

    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")  # Print the matrix
        print()

    for i in range(n):
        for j in range(1, n):
            if a[i][0] != a[i][j]:  # Check whether row has not same values
                isSameOnARow = False
    isSameOnARow = True

    for i in range(n):
        for j in range(n):
            if isSameOnARow:
                print("All ", str(a[i][0]) + "'s on row ", i)
            else:
                print("No same numbers on a row")


def getIt():
    pass


main()  # Invoke main function
