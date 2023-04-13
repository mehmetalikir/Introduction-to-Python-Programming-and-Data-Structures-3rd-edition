# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Assign grades) Write a program that reads student scores, gets the best score,
and then assigns grades based on the following scheme:
Grade is A if score is >= best - 10
Grade is B if score is >= best - 20;
Grade is C if score is >= best - 30;
Grade is D if score is >= best - 40;
Grade is F otherwise.'''


def main():
    # Prompt the user to enter all the scores
    s = input("Please enter scores separated by spaces from one line: ")  # 40 55 70 58
    items = s.split(" ")  # Extract items from the string
    list1 = [float(x) for x in items]  # Convert items to numbers

    for i in range(len(list1)):
        print(f"Student {i} score is {list1[i]} and grade is {getScore(max(list1), list1[i])}")


def getScore(best, score):
    # Assign grades based on the provided scheme
    if score >= best - 10:
        return 'A'
    elif score >= best - 20:
        return 'B'
    elif score >= best - 30:
        return 'C'
    elif score >= best - 40:
        return 'D'
    else:
        return 'F'


main()
