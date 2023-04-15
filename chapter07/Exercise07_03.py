# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Count occurrence of numbers) Write a program that reads the integers between 1
and 100 and counts the occurrences of each.

Note that if a number occurs more than one time, the plural word "times" is used
in the output'''


def main():
    # Create a list of characters
    list1 = createList()

    # Count the occurrences of each integer
    counts = countIntegers(list1)

    # Display counts
    print("The occurrences of each integer are: ")
    displayCounts(counts)


def createList():
    # Prompt the user to integers between 1 and 100
    s = input("Please enter ten numbers: ")  # 2 5 6 5 4 3 23 43 2

    # Read all the numbers and store them in list1
    list1 = [int(x) for x in s.split(" ")]  # Convert input to integer

    # Sort the elements in the list in ascending order.
    list1.sort()

    # Return the list
    return list1


# Count the occurrences of each integer
def countIntegers(list1):
    # Create a list of 100 to hold occurrence
    counts = 100 * [0]

    # For each integer in the list, count it
    for i in range(len(list1)):
        counts[list1[i] - 1] += 1

    return counts


# Display counts
def displayCounts(counts):
    for i in range(len(counts)):
        s = ""
        if counts[i] > 0:
            if counts[i] > 1:
                s = "s"
            print(f"{i + 1} occurs {counts[i]} time{s}")


main()  # Call main function
