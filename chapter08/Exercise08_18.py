# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Sample rows) Write a function that picks three sample of the rows in a two-dimensional list
using the following header:

    def pickSample(m):

Write a test program that shuffles the following matrix:
    m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]'''

import random


def main():
    nlist = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    pickSample(nlist)

    print(pickSample(nlist))


def pickSample(m):
    return random.sample(m, 3)


main()  # Invoke main function
