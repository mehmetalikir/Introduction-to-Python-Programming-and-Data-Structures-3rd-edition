# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the index of the largest element) Write a function that returns the index of
the largest element in a list of integers. If the number of such elements is
greater than 1, return the largest index. Use the following header:

def indexOfLargestElement(list):

Write a test program that prompts the user to enter a list of  numbers, invokes this
function to return the index of the largest element, and displays the index.'''


def main():
    # Create a list of numbers
    list1 = createList()

    # Get the index of the largest element in list
    index = indexOfLargestElement(list1)

    # Display the index
    displayIndex(index)


def createList():
    # Prompt the user to enter a list of  numbers
    s = input("Please enter a list of number: ")

    list1 = [int(x) for x in s.split(" ")]

    return list1


# Return the index of the largest element in a list of integers
def indexOfLargestElement(list1):
    # Assign values
    largest = 0
    index = 0

    for i in range(len(list1)):
       if list1[i] > largest:
           largest = list1[i]
           index = i

    return index


 # Display the index
def displayIndex(index):
    print("The index of the largest element is ", index)


main()  # Invoke main function
