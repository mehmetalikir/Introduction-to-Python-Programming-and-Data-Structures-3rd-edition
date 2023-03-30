# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Math: hexagonal numbers) A hexagonal number is defined as n(2n–1)  for
n = 1, 2, . . ., and so on. So, the first few numbers are 1, 6, 15, 28, . . . .
Write a function with the following header that returns a hexagonal number:

def getHexagonalNumber(n):

For example, getHexagonalNumber(1) returns 1 and getHexagonalNUmber(2) returns 6.
Write a test program that uses this function to display the first 50 hexagonal
numbers with 5 numbers on each line.'''


# Return a hexagonal number
def getHexagonalNumber(n):
    return n * (2 * n - 1)

def main():
    PER_LINE = 5  # Display 5 per line
    NUMBER_OF_HEXAGONAL = 50  # Count the number of hexagonal numbers

    # Display first 50 hexagonal numbers
    print("The first 50 hexagonal numbers are")
    for i in range(1, NUMBER_OF_HEXAGONAL, +1):
        print(getHexagonalNumber(i), end=" ")

        # Print 5 numbers per line
        if i % PER_LINE == 0:
            print()


main()  # Call the main function


