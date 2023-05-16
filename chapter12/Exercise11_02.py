# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(The Location class) Design a class named Location for locating a minimal
value and its location in a two-dimensional list. The class contains the public data
fields row, column, and minValue that store the minimum value and its indexes in
a two-dimensional list, with row and column as int types and minValue as a
float type.
Write the following method that returns the location of the smallest element in a
two-dimensional list.

    def Location locateSmallest(number):

The return value is an instance of Location. Write a test program that prompts
the user to enter a two-dimensional list and displays the location of the smallest element
in the list.'''


class Location:
    def __init__(self, row, column, minValue):
        self.row = row
        self.column = column
        self.minValue = minValue

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def getMinValue(self):
        return self.minValue


def main():
    row = int(input("Please enter the number of rows of the list: "))

    matrix = []
    for i in range(row):
        s = input("Please enter row " + str(i) + ": ")
        items = s.split()  # Extracts items from the string
        lst = [float(x) for x in items]  # Convert items to numbers
        matrix.append(lst)

    location = locateSmallest(matrix)
    print("The location of the smallest element is "
          + str(location.getMinValue()) + " at ("
          + str(location.getRow()) + ", " + str(location.getColumn()) + ")")


def locateSmallest(a):
    minValue = a[0][0]
    row = 0
    column = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if minValue > a[i][j]:
                minValue = a[i][j]
                row = i
                column = j

    return Location(row, column, minValue)


main()
