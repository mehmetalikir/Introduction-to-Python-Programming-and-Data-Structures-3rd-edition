# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Revise selection sort) In Section 7.10, you used selection sort to sort a list.
The selection-sort function repeatedly finds the smallest number in the current
list and swaps it with the first one. Rewrite this program by finding the largest number
and swapping it with the last one. Write a test program that reads in numbers
entered in one line, invokes the function, and displays the sorted numbers.'''


# The function for sorting elements in descending order
def selectionSort(lst):
    for i in range(len(lst) - 1):
        # Find the maximum in the lst[i : len(lst)]
        currentMax = max(lst[i:])
        currentMaxIndex = i + lst[i:].index(currentMax)

        # Swap lst[i] with lst[currentMaxIndex] if necessary
        if currentMaxIndex != 1:
            lst[currentMaxIndex], lst[i] = lst[i], currentMax


def main():
    # Create a list of numbers
    lst = [-2, 4.5, 5, 1, 2, -3.3]

    selectionSort(lst) # Invoke function

    # Display result
    print(lst)


main() # Invoke main function
