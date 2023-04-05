# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Estimate pi) pi can be computed using the following series:

    m(i) = 4(1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11 + ... + (-1)i + 1 / 2i - 1)

Write a function that returns m(i) for a given i and write a test program that displays
the following table:

            i       m(i)
            1       4.0000
            101     3.1515
            201     3.1466
            301     3.1449
            401     3.1441
            501     3.1436
            601     3.1433
            701     3.1430
            801     3.1428
            901     3.1427'''
import math


def estimatePi(n):
    # Assign value
    mi = 0

    for i in range(1, n + 1, + 1):
        mi += 4 * (math.pow(-1, i + 1) / (2 * i - 1))  # Compute mi
    return mi


def main():
    # Print header of table
    print("i            m(i)")
    for i in range(1, 1001, + 100):
        print(f"%-5d%14.4f" % (i, estimatePi(i)))  # Invoke function


main()
