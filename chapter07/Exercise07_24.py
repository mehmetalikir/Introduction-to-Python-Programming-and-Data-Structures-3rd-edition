# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Math: combinations) Write a program that prompts the user to enter a sentence
and displays all combinations of picking two words from the sentence.'''


def main():
    # Create a list from sentence
    lst = createList()

    # Display result
    displayResult(lst)


def createList():
    # Prompt the user to enter a sentence
    s = input("Please enter a sentence: ")

    lst = [x for x in s.split()]

    return lst


def displayResult(lst):
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            print(f"{lst[i]} - {lst[j]}")


main()
