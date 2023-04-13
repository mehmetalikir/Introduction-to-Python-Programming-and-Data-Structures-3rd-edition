# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Assign result) Write a program that reads a list of scores and then assign pass if
the score is equal or above average, otherwise assigns fail'''

import statistics


def main():
    # Prompt the user to enter all the scores
    s = input("Please enter scores separated by spaces from one line: ")  # 67 87 56 76 81 83 54 79
    list1 = [float(x) for x in s.split(" ")]  # Convert items to numbers

    for i in range(len(list1)):
        print(f"Student {i} score is {list1[i]} and grade is "
              f"{getResult(statistics.mean(list1), list1[i])}")


def getResult(average, score):
    # Assign pass if the score is equal or above average, otherwise assign fail
    if score >= average:
        return "Pass"
    else:
        return "Fail"


main()
