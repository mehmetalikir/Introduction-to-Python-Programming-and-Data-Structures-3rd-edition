# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Execution time for sorting) Write a program that obtains the execution time of
selection sort, bubble sort, merge sort, quick sort, heap sort, and radix sort for
input size 50,000, 100,000, 150,000, 200,000, 250,000, and 300,000. Your program
should create data randomly and print a table like this:

Array   Selection   Insertion   Bubble  Merge   Quick   Heap    Radix
Size    Sort        Sort        Sort    Sort    Sort    Sort    Sort
10000   38          33          107     3       2       24      10
20000   142         121         463     4       2       7       13
30000   121         91          1073    6       2       7       3'''

import random
import time

from Heap import Heap


# Selection sort algorithm implementation
def selectionSort(lst):
    for i in range(len(lst) - 1):
        # Find the minimum in the lst[i : len(lst)]
        currentMin = min(lst[i:])
        currentMinIndex = i + lst[i:].index(currentMin)

        # Swap lst[i] with lst[currentMinIndex] if necessary
        if currentMinIndex != i:
            lst[currentMinIndex], lst[i] = lst[i], currentMin


# Bubble sort algorithm implementation
def bubbleSort(lst):
    needNextPass = True

    k = 1
    while k < len(lst) and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False
        for i in range(len(lst) - k):
            if lst[i] > lst[i + 1]:
                # swap lst[i] with lst[i + 1]
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                needNextPass = True  # Next pass still needed


# Merge sort algorithm implementation
def mergeSort(lst):
    if len(lst) > 1:
        # Merge sort the first half
        firstHalf = lst[: len(lst) // 2]
        mergeSort(firstHalf)

        # Merge sort the second half
        secondHalf = lst[len(lst) // 2:]
        mergeSort(secondHalf)

        # Merge firstHalf with secondHalf into list
        merge(firstHalf, secondHalf, lst)


# Merge two sorted lists */
def merge(list1, list2, temp):
    current1 = 0  # Current index in list1
    current2 = 0  # Current index in list2
    current3 = 0  # Current index in temp

    while current1 < len(list1) and current2 < len(list2):
        if list1[current1] < list2[current2]:
            temp[current3] = list1[current1]
            current1 += 1
            current3 += 1
        else:
            temp[current3] = list2[current2]
            current2 += 1
            current3 += 1

    while current1 < len(list1):
        temp[current3] = list1[current1]
        current1 += 1
        current3 += 1

    while current2 < len(list2):
        temp[current3] = list2[current2]
        current2 += 1
        current3 += 1


# Quick sort algorithm implementation
def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1)


def quickSortHelper(lst, first, last):
    if last > first:
        pivotIndex = partition(lst, first, last)
        quickSortHelper(lst, first, pivotIndex - 1)
        quickSortHelper(lst, pivotIndex + 1, last)


# Partition lst[first..last]
def partition(lst, first, last):
    pivot = lst[first]  # Choose the first element as the pivot
    low = first + 1  # Index for forward search
    high = last  # Index for backward search

    while high > low:
        # Search forward from left
        while low <= high and lst[low] <= pivot:
            low += 1

        # Search backward from right
        while low <= high and lst[high] > pivot:
            high -= 1

        # Swap two elements in the list
        if high > low:
            lst[high], lst[low] = lst[low], lst[low]

    while high > first and lst[high] >= pivot:
        high -= 1

    # Swap pivot with lst[high]
    if pivot > lst[high]:
        lst[first] = lst[high]
        lst[high] = pivot
        return high
    else:
        return first


# Heap sort algorithm implementation
def heapSort(lst):
    heap = Heap()  # Create a Heap

    # Add elements to the heap
    for v in lst:
        heap.add(v)

    # Remove elements from the heap
    for i in range(len(lst)):
        lst[len(lst) - 1 - i] = heap.remove()


# Radix sort algorithm implementation
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


def generateRandomData(size):
    # Generate random data of the given size
    return [random.randint(1, 100) for _ in range(size)]


def measureExecutionTime(sort_func, data):
    # Measure the execution time for a sorting function on given data
    start_time = time.time()
    sort_func(data)
    end_time = time.time()
    return end_time - start_time


def printExecutionTimes():
    input_sizes = [50000, 100000, 150000, 200000, 250000, 300000]
    algorithms = {
        'Selection Sort': selectionSort,
        'Bubble Sort': bubbleSort,
        'Merge Sort': mergeSort,
        'Quick Sort': quickSort,
        'Heap Sort': heapSort,
        'Radix Sort': radixSort
    }

    print("Array Size\tSelection Sort\tBubble Sort\tMerge Sort\tQuick Sort\tHeap Sort\tRadix Sort")
    for size in input_sizes:
        data = generateRandomData(size)
        times = []
        for algorithm_name, algorithm_func in algorithms.items():
            execution_time = measureExecutionTime(algorithm_func, data.copy())
            times.append(execution_time)
        print(
            f"{size}\t\t{round(times[0], 3)}\t\t{round(times[1], 3)}\t\t{round(times[2], 3)}\t\t{round(times[3], 3)}\t\t{round(times[4], 3)}\t\t{round(times[5], 3)}")


printExecutionTimes()
