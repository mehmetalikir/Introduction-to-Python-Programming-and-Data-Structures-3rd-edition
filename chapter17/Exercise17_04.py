# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Radix sort) Write a program that randomly generates 100 three-digit integers and
sorts them in reverse order using radix sort.'''

import random


def main():
    numbers = []
    for i in range(100):
        numbers.append(random.randint(100, 999))

    radixSort(numbers, 3)
    print(numbers)


def radixSort(numbers, numberOfDigits):
    """Sort the int array list. numberOfDigits is the number of digits
       in the largest number in the list."""
    buckets = []
    for i in range(10):
        buckets.append([0])

    for position in range(numberOfDigits + 1):
        # Clear buckets
        for i in range(len(buckets)):
            buckets[i] = []

            # Distribute the elements from list to buckets
        for i in range(len(numbers)):
            key = getKey(numbers[i], position)
            buckets[key].append(numbers[i])

        # Now move the elements from the buckets back to list
        k = 0  # k is an index for list
        for i in reversed(range(len(buckets))):
            for j in range(len(buckets[i])):
                numbers[k] = buckets[i][j]
                k += 1


def getKey(number, position):
    """"Return the digit at the specified position.
        The last digit's position is 0."""
    result = 1
    for i in range(position):
        result *= 10

    return (number // result) % 10


main()
