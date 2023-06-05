# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Summing series) Write a recursive function to compute the following series:

    m(i) = 1 / 3 + 2 / 4 + ... + i / i + 2

Write a test program that prompts the user to enter an integer for i and displays m(i).'''


# Compute the series
def main():
    i = int(input("Please enter i: "))
    print("m(" + str(i) + ") is " + str(m(i)))


def m(i):
    if i == 1:  # Base case
        return 1.0 / 3
    return m(i - 1) + i * 1.0 / (i + 2)  # Recursive call


main()
