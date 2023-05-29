# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Count occurrences of numbers) Write a program that reads an unspecified number
of integers and finds the ones that have the most occurrences. For example, if
you enter 2 3 40 3 5 4 –3 3 3 2 0, the number 3 occurs most often. Enter all numbers
in one line. If not one but several numbers have the most occurrences, all of
them should be reported. For example, since 9 and 3 appear twice in the list 9 30
3 9 3 2 4, both occurrences should be reported.'''


def main():
    s = input("PLease enter the numbers: ").strip()
    numbers = [int(x) for x in s.split()]

    dictionary = {}  # Create an empty dictionary

    for number in numbers:
        if number in dictionary:
            dictionary[number] += 1
        else:
            dictionary[number] = 1

    maxCount = max(dictionary.values())

    pairs = list(dictionary.items())

    items = [[x, y] for (x, y) in pairs]  # Reverse pairs in the list

    print("The numbers with the most occurrence are ", end="")
    for (x, y) in items:
        if y == maxCount:
            print(x, end=" ")


main()
