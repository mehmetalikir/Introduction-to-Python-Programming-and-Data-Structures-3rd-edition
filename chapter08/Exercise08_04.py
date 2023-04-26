# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Compute the daily average hours for each employee) Suppose the weekly hours for all
employees are stored in a table. Each row records an employee’s seven-day work
hours with seven columns. For example, the following table stores the work hours
for eight employees. Write a program that displays employees and their average daily hours
in decreasing order of the average hours.'''


def main():
    matrix = [
        [2, 4, 3, 4, 5, 8, 8],
        [7, 3, 4, 3, 3, 4, 4],
        [3, 3, 4, 3, 3, 2, 2],
        [9, 3, 4, 7, 3, 4, 1],
        [3, 5, 4, 3, 6, 3, 8],
        [3, 4, 4, 6, 3, 4, 4],
        [3, 7, 4, 8, 3, 8, 4],
        [6, 3, 5, 9, 2, 7, 9]]

    # Create an empty list
    lst = []
    for i in range(len(matrix)):
        lst.append(avgHours(matrix[i]))

    selectionSort(lst)

    for i in range(len(lst)):
        print(f"%0.2f" % lst[i], "hours average in day")


# Average hours of each row
def avgHours(matrix):
    total = 0
    days = 0
    for row in matrix:
        days += 1
        total += row

    return total / days


# The function for sorting elements in descending order
def selectionSort(lst):
    for i in range(len(lst) - 1):
        # Find the maximum in the lst[i : len(lst)]
        currentMax = max(lst[i:])
        currentMaxIndex = i + lst[i:].index(currentMax)

        # Swap lst[i] with lst[currentMaxIndex] if necessary
        if currentMaxIndex != 1:
            lst[currentMaxIndex], lst[i] = lst[i], currentMax


main()  # Invoke main function
