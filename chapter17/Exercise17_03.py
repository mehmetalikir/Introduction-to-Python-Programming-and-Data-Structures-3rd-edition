# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Min-heap) The heap presented in the text is also known as a max-heap, in which
each node is greater than or equal to any of its children. A min-heap is a heap
in which each node is less than or equal to any of its children. Min-heaps are
often used to implement priority queues. Revise the Heap class to
implement a min-heap.'''

from Heap import Heap


def heapSort(lst):
    heap = Heap()  # Create a min-heap

    # Add elements to the heap
    for v in lst:
        heap.add(v)

    # Remove elements from the heap
    for i in range(len(lst)):
        lst[i] = heap.remove()


def main():
    numbers = input("Enter numbers separated by spaces: ").split()  # 1 2.4 2.5 2 1.5 34.5 5.5 6 6 2.4 5.5 9
    lst = [float(x) for x in numbers]
    heapSort(lst)
    for v in lst:
        print(v, end=" ")


main()
