# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Algebra: add two matrices) Write a function to add two matrices. The header of
the function is:

    def addMatrix(a, b):

In order to be added, the two matrices must have the same dimensions and the
same or compatible types of elements. Let c be the resulting matrix. Each element
cij is aij + bij. For example, for two 3 * 3 matrices a and b, c is

a11 a12 a13       b11 b12 b13       a11 + b11 a12 + b12 a13 + b13
a21 a22 a23   +   b21 b22 b23   =   a21 + b21 a22 + b22 a23 + b23
a31 a32 a33       b31 b32 b33       a31 + b31 a32 + b32 a33 + b33

Write a test program that prompts the user to enter two 3 x 3 matrices and displays
their sum. The matrices in each matrix are entered in one line.

1.0 2.0 3.0     0.0 2.0 4.0     1.0 4.0 7.0
4.0 5.0 6.0  +  1.0 4.5 2.2  =  5.0 9.5 8.2
7.0 8.0 9.0     1.1 4.3 5.2     8.1 12.3 14.2'''

import numpy as np

def main():
    s1 = (input(f"Please enter a 3-by-3 matrix1: "))  # 1 2 3 4 5 6 7 8 9
    a = getMatrix(s1)  # Get a list
    s2 = (input(f"Please enter a 3-by-3 matrix2: "))  # 0.0 2.0 4.0 1.0 4.5 2.2 1.1 4.3 5.2
    b = getMatrix(s2)  # Get a list

    # Display result
    c = addMatrix(a, b)

    print(f"{c}")



# Add two matrices
def addMatrix(a, b):
    c = np.add(a,b)
    return c

def getMatrix(s):
    # Create an empty list
    matrix = []

    # Assign values
    numberOfRows = 3
    numberOfColumns = 3
    index = 0

    # Prompt the user to enter values
    for row in range(numberOfRows):
        matrix.append([])
        for column in range(numberOfColumns):
            value = [float(x) for x in s.split()]
            matrix[row].append(value[index])
            index += 1

    return matrix


main()  # Invoke main function
