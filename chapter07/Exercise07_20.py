# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: multiple Eight Queens solutions) Programing Exercise 7.18 asks you
to find one solution for the Eight Queens puzzle. Write a program to count all
possible solutions for the Eight Queens problem and display all the solutions.'''


def main():
    count = 0  # How many solutions are found?

    # Queen positions
    queens = 8 * [-1]  # queens are placed at (i, queens[i])
    queens[0] = 0  # / Initially, place a queen at (0, 0) in the 0th row

    # k - 1 indicates the number of queens placed so far
    # We are looking for a position in the kth row to place a queen
    k = 1
    while k >= 0:
        # Find a position to place a queen in the kth row
        j = findPosition(k, queens)
        if j < 0:
            queens[k] = -1
            k -= 1  # back track to the previous row
        else:
            queens[k] = j;

            if k == 7:
                count += 1  # One more solution found
                print("Solution " + str(count) + ":")
                printResult(queens)
            else:
                k += 1

    print("How many solutions?", count)


def findPosition(k, queens):
    start = 0 if queens[k] == -1 else queens[k] + 1

    for j in range(start, 8):
        if isValid(k, j, queens):
            return j  # (k, j) is the place to put the queen now

    return -1


# Return true if you have a queen can be placed at (k, j)
def isValid(k, j, queens):
    # See if (k, j) is a possible position
    # Check jth column
    for i in range(0, k):
        if queens[i] == j:
            return False

    # Check major diagonal
    row = k - 1
    column = j - 1
    while row >= 0 and column >= 0:
        if queens[row] == column:
            return False
        row -= 1
        column -= 1

    # Check minor diagonal
    row = k - 1
    column = j + 1
    while row >= 0 and column <= 7:
        if queens[row] == column:
            return False
        row -= 1
        column += 1

    return True


# Print a two-dimensional board to display the queens
def printResult(queens):
    # Display the output
    for i in range(0, 8):
        for j in range(0, queens[i]):
            print("| ", end='')
        print("|Q|", end='')
        for j in range(queens[i] + 1, 8):
            print(" |", end='')
        print()


main()
