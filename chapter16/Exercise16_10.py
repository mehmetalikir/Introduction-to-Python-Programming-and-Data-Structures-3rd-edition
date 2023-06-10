# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Execution time based on operator) Do you think different operators have different
execution times (for instance is addition faster than multiplication)? Amend
the program you wrote for Programming Exercise 16.6 such that in addition to
adding the integers, you have separate functions that apply multiplication and
modulo. Check how the execution times of the different operators compare.'''

import time


def main():
    for n in [10_000, 100_000, 1_000_000, 10_000_000, 1_00_000_000]:
        print(n)
        print(f"\tAdd      took {getTimeAdd(n)} seconds")
        print(f"\tMultiply took {getTimeMult(n)} seconds")
        print(f"\tModulo   took {getTimeMod(n)} seconds")


def getTimeAdd(n):
    startTime = time.time()
    total = 0
    for i in range(n):
        total += i
    endTime = time.time()
    return endTime - startTime


def getTimeMult(n):
    startTime = time.time()
    total = 0
    for i in range(n):
        total *= i
    endTime = time.time()
    return endTime - startTime


def getTimeMod(n):
    startTime = time.time()
    total = 0
    for i in range(1, n):
        total %= i
    endTime = time.time()
    return endTime - startTime


main()
