# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the lowest number in a list) Write a recursive that returns the
smallest number in a list. Write a main program that prompt the user to enter a
series of numbers separated by spaces and displays the smallest one.'''


def main():
    s = input("Please enter numbers separated by spaces on one line: ")
    items = s.split()  # Extract items from the string
    numbers = [float(x) for x in items]  # Convert items to numbers

    # Display the smallest one
    print(f"The smallest number in {numbers} is {smallest(numbers)}")


# Return the smallest number in a list
def smallest(numbers):
    return smallestHelper(numbers, len(numbers) - 1)


# Overloaded helper function
def smallestHelper(numbers, index):
    if index == 0:
        return numbers[0]
    return min(smallestHelper(numbers, index - 1), numbers[index])


main()
