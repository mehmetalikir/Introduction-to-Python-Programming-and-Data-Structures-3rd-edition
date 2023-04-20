# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Bubble sort) Write a sort function that uses the bubble-sort algorithm. The bubble-
sort algorithm makes several passes through the list. On each pass, successive
neighboring pairs are compared. If a pair is in decreasing order, its values are swapped;
otherwise, the values remain unchanged. The technique is called a bubble sort or
sinking sort because the smaller values gradually “bubble” their way to the top
and the larger values “sink” to the bottom. Write a test program that reads in numbers
entered in one line, invokes the function, and displays the sorted numbers.'''


def main():
    # Create a list of numbers
    lst = createList()

    # Display result
    displayResult(lst)


def createList():
    # Prompt the user to enter list of numbers
    s = input("Please enter numbers: ")  # 64 78 4 70 52 4 76 52 91 44 806 22
    lst = [int(x) for x in s.split(" ")]

    return lst


# Display result
def displayResult(lst):
    print(bubblesort(lst))  # Invoke function


# The function for sorting elements in ascending order
def bubblesort(lst):
    swapped = True
    while swapped:
        # Check whether all elements sorted
        swapped = False
        for i in range(len(lst) - 1):
            # Swap lst[i] with lst[i + 1] if necessary
            if lst[i] > lst[i + 1]:
                lst[i + 1], lst[i] = lst[i], lst[i + 1]
                swapped = True
    return lst


main()  # Invoke main function
