# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Write/read data) Write a program that writes 100 integers created randomly into
a file. Integers are separated by a space in the file. Read the data back from the file
and display the sorted data. Your program should prompt the user to enter a filename.
If the file already exists, do not override it.'''

import os.path
from random import randint


def main():
    # Prompt the user to enter filename
    f1 = input("Enter a filename: ").strip()

    # Check whether file is exist or not
    if os.path.isfile(f1):
        print("The file already exists")
        return

    # Open file for output
    outputFile = open(f1, "w")

    for i in range(100):
        print(randint(0, 999), file=outputFile, end=" ")

    outputFile.close()

    inputFile = open(f1, "r")
    s = inputFile.read()  # Read all from the file

    numbers = [int(items) for items in s.split()]
    numbers.sort()

    for i in range(len(numbers)):
        print(numbers[i], end=" ")

    inputFile.close()  # Close the output file


main()
