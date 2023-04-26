# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Average the major diagonal in a matrix) Write a function that finds average of
the numbers of the major diagonal in an n x n matrix of integers using the
following header:

    def avgMajorDiagonal(m):

The major diagonal is the diagonal that runs from the top left corner to the bottom
right corner in the square matrix. Write a test program that reads a 4 x 4 matrix and
displays the average of elements on the major diagonal.
7 9 5 2
8 3 7 0
2 6 1 7
3 9 7 5'''


def main():
    m = getMatrix()  # Get a list

    # Display the average of elements on the major diagonal
    print(f"Average of the elements in the "
          f"major diagonal is {avgMajorDiagonal(m)}")


# Get average of the numbers
def avgMajorDiagonal(m):
    # Assign value
    sum = 0.0
    numbers = 0

    # Find the numbers of the major diagonal in matrix
    for i in range(len(m)):
        for j in range(len(m[i])):
            numbers = len(m[i])
            if i == j:
                sum += m[j][i]

    return sum / numbers


def getMatrix():
    # Create an empty list
    matrix = []

    # Assign values
    numberOfRows = 4
    numberOfColumns = 4

    # Prompt the user to enter values
    for row in range(numberOfRows):
        matrix.append([])
        s = (input(f"Please enter a 4-by-4 matrix row {row}: "))
        for column in range(numberOfColumns):
            value = [float(x) for x in s.split()]
            matrix[row].append(value[column])

    return matrix


main()  # Invoke main function
