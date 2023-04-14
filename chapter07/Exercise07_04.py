# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Analyze integers) Write a program that reads an unspecified number of integers
and determines how many integers are even and how many integers are odd.
Assume the input numbers are separated by one space in one line.'''


def main():
    # Create a list of integers
    list1 = createList()

    # Display result
    findEvenAndOdd(list1)


# Create a list of integers
def createList():
    # Prompt the user to integers between 1 and 100
    s = input("Please enter the numbers: ")  # 56 87 2 98 543 -5 762

    # Read integers and add them to the list
    list1 = [int(x) for x in s.split(" ")]  # Convert input to integer

    # Sort the elements in the list in ascending order.
    list1.sort()

    # Return the list
    return list1

# Display the count of even and odd integers
def findEvenAndOdd(list1):
    # Assign values
    evens = 0
    odds = 0

    # Check whether number is even or odd
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            evens += 1
        else:
            odds += 1

    # Display result
    print("Total number of even integers: ", evens)
    print("Total number of odd integers: ", odds)


main()  # Call main function
