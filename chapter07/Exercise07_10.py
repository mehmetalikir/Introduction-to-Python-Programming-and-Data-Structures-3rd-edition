# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Reverse a list) The reverse function in Section 7.8 reverses a list by
copying it to a new list. Rewrite the function that reverses the list passed in
the argument and returns this list. Write a test program that prompts the user to
enter a list of numbers, invokes the function to reverse the numbers, and displays the
numbers.'''


def main():
    # Create a list of numbers
    list1 = createList()

    # Displays the mean and standard deviation
    displayResult(list1)


def createList():
    # Prompt the user to enter list of numbers
    s = input("Please enter numbers: ")  # 1.9 2.5 3.7 2 1.5 6 3 4 5 2.5
    list1 = [float(x) for x in s.split(" ")]

    return list1


# Display result
def displayResult(list1):
    print(reverse(list1))


def reverse(list1):
    # Create an empty list
    reversed = []

    for i in range((len(list1) - 1), -1, -1):
        reversed.append(list1[i])

    return reversed


main()  # Invoke main function
