# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Column sorting) Implement the following function to sort the columns in a two-dimensional
list. A new list is returned and the original list is intact.

    def sortColumns(m):

Write a test program that prompts the user to enter a 3 x 3 matrix of numbers and
displays a new column-sorted matrix.'''


def main():
    # m = [[1, 4, 8],
    #      [7, 9, 0],
    #      [5, 2, 6]]

    SIZE = 3
    print("Enter a 3 by 3 matrix row by row: ")
    m = []

    for i in range(SIZE):
        line = input().split()
        m.append([float(x) for x in line])

    # Display a new column-sorted matrix
    print("The column-sorted list is ")
    printMatrix(sortColumns(m))


def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[j][i], end=" ")
        print()


def sortColumns(m):
    import pandas as pd
    df = pd.DataFrame(data=m)
    for col in df:
        df[col] = df[col].sort_values(ignore_index=True)  # (by= df.columns[0])

    return df


main()  # Invoke main function
