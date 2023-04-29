# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Locate the smallest element) Write the following function that returns the location
of the largest element in a two-dimensional list:

    def locateSmallest(a):

The return value is a one-dimensional list that contains two elements. These
two elements indicate the row and column indexes of the smallest element in the
two-dimensional list. Write a test program that prompts the user to enter a two-dimensional
list and displays the location of the smallest element in the list.'''


def main():
    # Create a list of numbers
    a = createList()

    locateSmallest(a)


def createList():
    # Prompt the user to enter the numbers of matrix
    numberOfRows = int(input("Please enter the number of row in the list: "))

    # Create an empty list
    matrix = [[]] * numberOfRows

    for i in range(numberOfRows):
        # Prompt the user to enter the rows
        s = input("Please enter a row : ")
        matrix[i] = [int(x) for x in s.split(" ")]

    return matrix


# Display the location of the smallest element in the list
def locateSmallest(a):
    # Assign values
    smallest = 1_000_000_000
    indexRow = 0
    indexCol = 0

    # Find the smallest element and its indices
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] < smallest:
                smallest = a[i][j]  # Swap it
                indexRow = i
                indexCol = j

    print(f"The location of the smallest{smallest} element is at ({indexRow},{indexCol})")


main()  # Invoke main function
