# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Execution time for quadratic time algorithm) Write an algorithm that calculates
the sum of integers for a given number(n(n + 1)/2). Then implement a second
algorithm that calculates the sum of the sums of digits in a series between 0
and given number (e.g, 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 + 1 + 1
+ 1 + 2...). Create a test program that invokes the two algorithms with 1_000
10_000, 100_000 and 1_000_000. Compare the execution times of the two algorithms.'''

import time


# This function calculates the sum of integers for a given number
def getTime(n):
    total = 0
    for i in range(n):
        total += i
    return


# Calculates the sum of the sums of digits in a series between 0 and a given number
def getTimeQuad(n):
    startTime = time.time()
    total = 0
    for i in range(n):
        digit = i
        while (digit > 0):
            digit = digit // 10
            total += digit
    endTime = time.time()
    return endTime - startTime


def main():
    print("10000")
    startTime = time.time()
    getTime(10000)
    executionTime = time.time() - startTime
    print(f"\t{executionTime} seconds")
    startTime = time.time()
    getTimeQuad(10000)
    executionTime = time.time() - startTime
    print(f"\t{executionTime} seconds")

    print("100000")
    startTime = time.time()
    executionTime = time.time() - startTime
    getTime(100000)
    print(f"\t{executionTime} seconds")
    startTime = time.time()
    getTimeQuad(100000)
    executionTime = time.time() - startTime
    print(f"\t{executionTime} seconds")

    print("1000000")
    startTime = time.time()
    executionTime = time.time() - startTime
    getTime(1000000)
    print(f"\t{executionTime} seconds")
    startTime = time.time()
    getTimeQuad(1000000)
    executionTime = time.time() - startTime
    print(f"\t{executionTime} seconds")

    print("10000000")
    startTime = time.time()
    getTime(10000000)
    executionTime = time.time() - startTime
    print(f"\t{executionTime} seconds")

    # While the calls above are likely to execute extremely fast, this one may take some time to execute
    startTime = time.time()
    getTimeQuad(10000000)
    executionTime = time.time() - startTime
    print(f"\t{executionTime} seconds")


main()

