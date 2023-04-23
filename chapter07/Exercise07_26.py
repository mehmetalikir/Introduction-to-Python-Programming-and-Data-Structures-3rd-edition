# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Merge two sorted lists) Write the following function that merges two sorted lists
into a new sorted list.

    def merge(list1, list2):

Implement the function in a way that takes len(list1) + len(list2) comparisons
Write a test program that prompts the user to enter two sorted lists and
displays the merged list.'''


def main():
    # Prompt the user to enter list of integers
    s1 = input("Please enter integers for list1: ")
    s2 = input("Please enter integers for list2: ")
    list1 = [int(x) for x in s1.split(" ")]  # 5 21 55 62 71 76
    list2 = [int(x) for x in s2.split(" ")]  # 5 12 15 16 21 26

    # Displays the merged list
    print("The merged list is ", end=""), merge(list1, list2)


def merge(list1, list2):
    # Sort the lists
    list1.sort()
    list2.sort()

    # Merge two sorted lists into a new sorted list
    list1.extend(list2)
    list1.sort()

    for i in range(0, len(list1)):
        print(list1[i], end=" ")


main()
