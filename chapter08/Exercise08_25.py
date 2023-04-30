# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Markov matrix) An n x n matrix is called a positive Markov matrix if each element
is positive and the sum of the elements in each column is 1. Write the following
function to check whether a matrix is a Markov matrix:

    def isMarkovMatrix(m):

Write a test program that prompts the user to enter a 3 x 3 matrix of numbers and
tests whether it is a Markov matrix.'''


def main():
    # Prompt the user to enter a 3 x 3 matrix of numbers
    m = [[0.15, 0.875, 0.375],
         [0.55, 0.005, 0.225],
         [0.30, 0.12, 0.4]]

    isMarkovMatrix(m)


def isMarkovMatrix(m):
    # Check columns
    for j in range(3):
        sum = 0
        for i in range(3):
            sum += m[i][j]
            if sum == 1:
                print("It is a Markov matrix")


main()  # Invoke main function
