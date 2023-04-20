# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: Eight Queens) The classic Eight Queens puzzle is to place eight queens
on a chessboard such that no two queens can attack each other (i.e., no two queens
are on the same row, same column, or same diagonal). There are many possible
solutions. Write a program that displays one such solution.'''


def main():
    # Create a list of characters
    lst = createList()

    # Display result
    displayResult(lst)


def createList():
    # Create a list of 8 to hold Q and space
    lst = 8 * [0]

    return lst


# Display result
def displayResult(lst):
    for i in range(len(lst)):
        print("|")
        for j in range(len(lst)):
            if isQueen():
                print("Q|")
            else:
                print(" |")


# TO-DO
def isQueen():
    return True


main()  # Call main function
