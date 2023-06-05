# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Sum series) Write a recursive function to compute the following series:

    m(i) = 1 / 3 + 2 / 5 + 3 / 7 + ... + i / 2i + 1

Write a test program that displays m(i) for i 1, 2, ..., 10.'''


# Compute the series
def main():
    print(f"i\t\tm(i)")
    for i in range(1, 10):
        print(f"{i}\t\t{m(i)}")


def m(i):
    if i == 0:
        return 0  # Base case
    else:
        return i / (2 * i + 1) + m(i - 1)  # Recursive call


main()
