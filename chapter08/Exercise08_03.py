# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Sort students by grades) Rewrite Listing 8.2, GradeExam.py, to display the students
in increasing order of the number of correct answers.'''


def main():
    # Create a list
    students = gradeExam()

    selectionSort(students) # Sort the students in increasing order of the number of correct answers

    # Display result
    for i in range(len(students)):
        print("Student", i, "'s correct count is", students[i])


def gradeExam():
    # Students' answers to the questions
    answers = [
        ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
        ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
        ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
        ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]

    # Key to the questions
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']

    # Hold students' scores
    studensScores = [0] * len(answers)

    # Grade all answers
    for i in range(len(answers)):
        # Grade one student
        correctCount = 0
        for j in range(len(answers[i])):
            if answers[i][j] == keys[j]:
                correctCount += 1

        studensScores[i] = correctCount

    return studensScores


# The function for sorting elements in ascending order
def selectionSort(lst):
    for i in range(len(lst) - 1):
        # Find the minimum in the lst[i : len(lst)]
        currentMin = min(lst[i:])
        currentMinIndex = i + lst[i:].index(currentMin)

        # Swap lst[i] with lst[currentMinIndex] if necessary
        if currentMinIndex != 1:
            lst[currentMinIndex], lst[i] = lst[i], currentMin


main()  # Call the main function
