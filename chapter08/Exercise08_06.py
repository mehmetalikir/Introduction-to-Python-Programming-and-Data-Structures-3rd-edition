# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Algebra: multiply two matrices) Write a method to multiply two matrices. The
header of the method is:

    def multiplyMatrix(a,b)

To multiply matrix a by matrix b, the number of columns in a must be the same as
the number of rows in b, and the two matrices must have elements of the same or
compatible types. Let c be the result of the multiplication. Assume the column size
of matrix a is n. Each element cij is ai1 * b1j + ai2 * b2j + c + ain * bnj.
For example, for two 3 * 3 matrices a and b, c is

a11 a12 a13       b11 b12 b13       a11 + b11 a12 + b12 a13 + b13
a21 a22 a23   +   b21 b22 b23   =   a21 + b21 a22 + b22 a23 + b23
a31 a32 a33       b31 b32 b33       a31 + b31 a32 + b32 a33 + b33

where cij = ai1 * b1j + ai2 * b2j + ai3 * b3j.

Write a test program that prompts the user to enter two 3 x 3 matrices and displays
their product.

1.0 2.0 3.0     0.0 2.0 4.0     1.0 4.0 7.0
4.0 5.0 6.0  +  1.0 4.5 2.2  =  5.0 9.5 8.2
7.0 8.0 9.0     1.1 4.3 5.2     8.1 12.3 14.2'''


def main():
    s1 = (input(f"Please enter a 3-by-3 matrix1: "))  # 1 2 3 4 5 6 7 8 9
    a = getMatrix(s1)  # Get a list
    s2 = (input(f"Please enter a 3-by-3 matrix2: "))  # 0.0 2.0 4.0 1.0 4.5 2.2 1.1 4.3 5.2
    b = getMatrix(s2)  # Get a list

    # Display result
    c = multiplyMatrix(a, b)

    print(f"{c}")


# Multiply two matrices
def multiplyMatrix(a, b):
    lst = [0] * len(b[0])
    c = []
    for i in range(len(a)):
        c.append([x for x in lst])

    for i in range(len(c)):
        for j in range(len(c[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

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
