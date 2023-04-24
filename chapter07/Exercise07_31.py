# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Occurrence of each digit in a string) Write a program that counts the occurrences
of each digit in a string using the following header:

    def count(s):

The function counts how many times a digit appears in the string. The return
 value is a list of ten elements, each of which holds the count for a digit. For
 example, after executing counts = count("12203AB3"), counts[0] is 1,
 counts[1] is 1, counts[2] is 2, and counts[3] is 2. Write a test program that
 prompts the user to enter a string and displays the number of occurrences of each
 digit in the string.'''


def main():
    # Create a list of digit
    lst = createList()

    # Count the occurrences of each digit
    counts = countDigit(lst)

    # Display counts
    print("The occurrences of each digit are: ")
    displayCounts(counts)


def createList():
    # Prompt the user to enter a string
    s = input("Please enter a string: ") # 12203AB3

    # Create an empty list
    lst = []

    for i in range(0, len(s)):
        if s[i].isdigit():
            lst.append(s[i])

    lst2 = [int(x) for x in lst] # Convert input to integer

    # Return the list
    return lst2


# Count the occurrences of each digit
def countDigit(lst):
    # Create a list to hold occurrence
    counts = 10 * [0]

    # For each digit in the list, count it
    for i in range(len(lst)):
        counts[lst[i]] += 1

    return counts


# Display counts
def displayCounts(counts):
    for i in range(len(counts)):
        s = ""
        if counts[i] > 0:
            if counts[i] > 1:
                s = "s"
            print(f"{i} occurs {counts[i]} time{s}")


main()  # Call main function
