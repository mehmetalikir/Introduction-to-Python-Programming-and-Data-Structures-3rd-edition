# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Compute lcm) Write a function that returns the least common multiple(lcm) of
integers in a list. Use the following header:

    def lcm(numbers):

Write a test program that prompts the user to enter a list of numbers, invokes the
function to find the lcm of these numbers, and display the lcm'''
import math


def main():
    # Create a list of numbers
    numbers = createList()

    # Displays the lcm
    displayResult(numbers)


def createList():
    # Prompt the user to enter list of numbers
    s = input("Please enter numbers: ")  # 1 9 2 5 3 7 2 1 5 6 3 4 5 2 45 5
    numbers = [int(x) for x in s.split(" ")]

    # Sort the elements in the list in ascending order.
    numbers.sort(reverse=True)

    return numbers


# Display result
def displayResult(numbers):
    print(lcm(numbers))


# Compute lcm of numbers
def lcm(numbers):
    # lcm = max(numbers)
    # numbers = removeDuplicate(numbers)  # -> 1, 2, 3, 4, 5, 6, 7, 9, 45
    # for i in range((len(numbers))):
    #     if lcm % numbers[i] != 0:
    #         lcm *= numbers[i]
    #     else:
    #         continue


    return math.lcm(*numbers)


# # Remove duplicate numbers in the list
# def removeDuplicate(numbers):
#     # Create an empty list
#     removed = []
#
#     for i in range(len(numbers)):
#         if numbers[i] not in removed:
#             removed.append(numbers[i])
#
#     return removed


main()  # Invoke main function
