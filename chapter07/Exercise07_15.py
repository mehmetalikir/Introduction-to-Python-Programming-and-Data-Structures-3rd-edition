# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Is the list even?) Write the following function that returns true if all the elements
in the list are even, otherwise return false:

    def isEven(lst):

Write a test program that prompts the user to enter a list and displays whether the
list is even or not'''


def main():
    # Create a list of numbers
    lst = createList()

    # Display result
    displayResult(lst)


def createList():
    # Prompt the user to enter list of numbers
    s = input("Please enter numbers: ")  # 64 78 4 70 54 # 52 76 91 44 806 22
    lst = [int(x) for x in s.split(" ")]

    return lst


# Display result
def displayResult(lst):
    if isEven(lst):
        print("The list is even")
    else:
        print("The list is not even")


# Return true if all the elements in the list are even, otherwise return false
def isEven(lst):
    odds = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            odds += 1

    if odds >= 1:
        return False
    else:
        return True


main()  # Invoke main function
