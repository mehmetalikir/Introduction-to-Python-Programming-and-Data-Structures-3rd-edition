# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Merge sort) Change the implementation of Programming Exercise 17.1 to use a
merge sort instead of a bubble sort.'''

def main():
    inputFile = open("test_results.txt", "r")

    records = []
    for line in inputFile:
        parts = line.strip().split(',')
        records.append([parts[0], [int(part) for part in parts[1:]]])
    inputFile.close()

    print("Before: ")
    print(records)
    mergeSort(records)
    for k in range(len(records)):
        mergeSort(records[k][1])
    print("After: ")
    print(records)


def mergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        mergeSort(left)
        mergeSort(right)
        # Two iterators for traversing the left and right half
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1


main()

