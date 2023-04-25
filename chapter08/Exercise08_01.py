# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Maximum elements per column) Write a function that returns the maximum of
all the elements in a specified column in a matrix using the following header:

    def maxColumn(m, columnIndex)

Write a test program that reads a 3 x 4 matrix and displays the maximum of each
column
12 63 59 82
75 65 92 52
41 73 63 88'''


def main():
    m = getMatrix()  # Get a list

    columnIndex = 0

    # Display result
    for columnIndex in range(len(m[0])):
        print(f"Maximum of the elements at column "
              f"{columnIndex} is {maxColumn(m, columnIndex)}")


# Return the maximum of all the elements in a specified column in a matrix
def maxColumn(m, columnIndex):
    # Assign value
    maxNum = 0.0

    # Find maximum element at column
    for i in range(len(m)):
        if m[i][columnIndex] > maxNum:
            maxNum = m[i][columnIndex]


    return maxNum


def getMatrix():
    # Create an empty list
    matrix = []

    # Assign values
    numberOfRows = 3
    numberOfColumns = 4

    # Prompt the user to enter values
    for row in range(numberOfRows):
        matrix.append([])
        s = (input(f"Please enter a 3-by-4 matrix row {row}: "))
        for column in range(numberOfColumns):
            value = [float(x) for x in s.split()]
            matrix[row].append(value[column])

    return matrix


main()  # Invoke main function
