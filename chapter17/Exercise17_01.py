# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Nested bubble sort) Write a program which reads test results from a text file and
sorts them by teh person who took the test then the test results themselves.
The sorting should be implemented as a bubble sort.
    The text file contains records in the following format(the name followed by
four test scores):

    Markus, 45, 47, 65, 77
    Ariana, 99, 53, 87, 43
    Eric, 19, 91, 65, 67
    Irena, 95, 91, 87, 67

    Load the results into a multidimensional list, such as:
    [['Markus', ['45', '47', '65', '77']]

After performing the sorts, the results should be printed.'''


def nestedBubbleSort(testResults):
    n = len(testResults)

    for i in range(n):
        for j in range(n - i - 1):
            if testResults[j][0] > testResults[j + 1][0]:
                testResults[j], testResults[j + 1] = testResults[j + 1], testResults[j]

    for i in range(n):
        for j in range(len(testResults[i][1])):
            for k in range(len(testResults[i][1]) - j - 1):
                if testResults[i][1][k] > testResults[i][1][k + 1]:
                    testResults[i][1][k], testResults[i][1][k + 1] = testResults[i][1][k + 1], testResults[i][1][k]

    return testResults


def loadTestResults(file_name):
    testResults = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            parts = line.split(', ')
            name = parts[0]
            scores = parts[1:]
            testResults.append([name, scores])

    return testResults


def printTestResults(testResults):
    for result in testResults:
        print(result[0] + ': ' + ', '.join(result[1]))


def main():
    fileName = 'test_results.txt'  # Replace with the actual file name
    testResults = loadTestResults(fileName)
    sortedResults = nestedBubbleSort(testResults)
    printTestResults(sortedResults)


if __name__ == '__main__':
    main()
