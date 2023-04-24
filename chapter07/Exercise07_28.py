# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Partition of a list) Write the following function that partitions the list using the
first element, called a pivot:

    def partition(lst):

After the partition, the elements in the list are rearranged so that all the elements
before the pivot are less than or equal to the pivot and the elements after the pivot
are greater than the pivot. The function also returns the index where the pivot is located
in the new list. For example, suppose the list is {5, 2, 9, 3, 6, 8}. After the partition,
the list becomes {3, 2, 5, 9, 6, 8}. Implement the function in a way that takes
len(lst) comparisons. Write a test program that prompts the user to
enter a list in one line and displays the list after the partition.'''


def main():
    # Prompt the user to enter list of numbers
    s = input("Please enter an integer list: ")  # 5, 2, 9, 3, 6, 8
    lst = [int(x) for x in s.split(",")]

    # Display the list after the partition
    print("After the partition, the list is", partition(lst))


# Partition the list using the pivot
def partition(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] < lst[0]:
            lst[i + 1], lst[0] = lst[0], lst[i + 1]

    return lst


main()  # Invoke main function
