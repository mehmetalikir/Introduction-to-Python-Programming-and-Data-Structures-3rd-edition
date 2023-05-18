# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Process scores in a text file) Suppose that a text file contains an unspecified number
of scores. Write a program that reads the scores from the file and displays their
total and average. Scores are separated by blanks. Your program should prompt
the user to enter a filename.'''


def main():
    # Prompt the user to enter filename
    f1 = input("Enter a filename: ").strip()

    # Open file for input
    inputFile = open(f1, "r")
    s = inputFile.read()  # Read all from the file

    numbers = [int(items) for items in s.split()]

    total = 0
    for i in range(len(numbers)):
        print(numbers[i], end=" ")
        total += numbers[i]

    print()
    print(f"Total: {total} and Average: %0.2f" % (total / len(numbers)))


main()
