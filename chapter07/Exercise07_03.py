# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Count occurrence of numbers) Write a program that reads the integers between 1
and 100 and counts the occurrences of each.

Note that if a number occurs more than one time, the plural word "times" is used
in the output'''


def main():
    # Prompt the user to integers between 1 and 100
    s = input("Please enter the integer between 1 and 100: ")  # 2 5 6 5 4 3 23 43 2
    list1 = [int(x) for x in s.split(" ")]  # Convert input to integer

    # Sort the elements in the list in ascending order.
    list1.sort()

    # Counts the occurrences of each
    for i in range(len(list1)):
        counts = list1.count(list1[i])  # For each integer in the list, count i
        string = ""
        if counts >= 2:
            string = "s"
        print(f"{list1[i]} occurs {counts} time{string}") # TO-DO


main()
