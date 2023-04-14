# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Print distinct numbers) Write a program that reads in integers separated by a
space in one line and displays distinct numbers in their input order and separated
by exactly one space (i.e., if a number appears multiple times, it is displayed only
once). (Hint: Read all the numbers and store them in list1. Create a new list
list2. Add a number in list1 to list2. If the number is already in the list,
ignore it.)'''


def main():
    # Create a list of integers
    list1 = createList()

    # Create an empty list
    list2 = []

    # Display result
    copyList(list1, list2)



# Create a list of integers
def createList():
    # Prompt the user to integers between 1 and 100
    s = input("Please enter ten numbers: ")  # 1 2 3 2 1 6 3 4 5 2

    # Read all the numbers and store them in list1
    list1 = [int(x) for x in s.split(" ")]  # Convert input to integer

    # Sort the elements in the list in ascending order.
    list1.sort()

    # Return the list
    return list1

# Display distinct numbers
def copyList(list1, list2):

    # Copy of list1 into list2 If the number is already in the list, ignore it
    for i in range(len(list1)):
        addDistinct(list1[i], list2)

    # Print distinct numbers
    print("The number of distinct numbers is", len(list2))
    print("The distinct numbers are: " , end=""), getDistinct(list2)


    # list2 = [x for x in list1] or list2 = [] + list1 or list2 = list1[ : ]


# Add distinct numbers into new list
def addDistinct(x, lst):
    if x not in lst:
        lst.append(x)

# Get distinct number from list2
def getDistinct(list2):
    for i in range(len(list2)):
        print(list2[i], end=" ")

main()  # Call main function
