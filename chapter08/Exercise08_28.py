# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Check for square of list) The lsit m2 is the square of the list m1 if each element
of m2 is equal to the square of the corresponding element in m1. Write a function
that returns True if all the elements of m2 are square of the corresponding elements
of m1, using the following header:

    def isSquare(m1, m2):

Write a test program that prompts the user two lists of integers and display
whether the second list is square of first or not.'''



def main():
    m1 = input("List1: please enter numbers: ").split() # 2 3 5 7 9
    m2 = input("List2, please enter squares of list1: ").split() # 4 9 25 49 81

    if isSquare(m1, m2):
        print("list2 is square of list1")
    else:
        print("list2 is not square of list1")


def isSquare(m1, m2):
    for i in range(len(m1)):
        if int(m2[i]) != int(m1[i]) * int(m1[i]): return False

    return True


main()  # Invoke main function
