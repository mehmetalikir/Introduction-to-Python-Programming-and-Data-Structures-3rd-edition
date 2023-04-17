# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Count single digits) Write a program that generates 1_000 random integers between
0 and 9 and displays the count for each number. (Hint: Use a list of ten integers,
say counts, to store the counts for the number of 0s, 1s, . . . , 9s.)'''

import random

RANDOM_INTEGERS = 1_000


def main():
    # Create a list of integers
    list1 = createList()

    # Count the occurrences of each number
    counts = countIntegers(list1)

    # Display counts
    print("The occurrences of each integer are: ")
    displayCounts(counts)


# Create a list of integers
def createList():
    # Create an empty list
    list1 = []

    for i in range(0, RANDOM_INTEGERS):
        list1.append(getRandomInteger())

    # Return the list
    return list1


# Count the occurrences of each integer
def countIntegers(list1):
    count = 10 * [0]
    for i in range(len(list1)):
        count[list1[i]] += 1

    return count


# Display the list
def displayCounts(counts):
    for i in range(len(counts)):
        s = ""
        if counts[i] >= 2:
            s = "s"
        print(f"{i} randomized {counts[i]} time{s} in {RANDOM_INTEGERS}")


# Generates random integers between 0 and 9
def getRandomInteger():
    return random.randint(0, 9)


main()  # Call main function
