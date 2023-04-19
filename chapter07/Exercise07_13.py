# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Swap smallest and largest) Write a function that returns a new list by swapping the
smallest element with the largest element in the list. Use the following function header:

    def smallestLargestSwap(lst):

Write a test program that reads in a list of integers, invokes the function, and
displays the result'''


def main():
    # Create a list of numbers
    numbers = createList()

    # Display result
    displayResult(numbers)


def createList():
    # Prompt the user to enter list of numbers
    s = input("Please enter numbers: ")  # 65 78 23 58 85 71 94 47 68 39
    numbers = [int(x) for x in s.split(" ")]

    return numbers


# Display result
def displayResult(numbers):
    print(smallestLargestSwap(numbers))


# Swap the smallest element with the largest element in the list
def smallestLargestSwap(numbers):
    # Assign index of values
    a = numbers.index(min(numbers))
    b = numbers.index(max(numbers))

    # Swap values in the list
    numbers[b], numbers[a] = numbers[a], numbers[b]  # Simultaneous assignment

    return numbers


main()  # Invoke main function
