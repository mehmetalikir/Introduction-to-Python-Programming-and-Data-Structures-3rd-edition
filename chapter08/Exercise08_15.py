# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: same line?) Exercise 6.19 gives a function for testing whether three
points are on the same line. Write the following function to test whether all the
points in the points list are on the same line:

    def sameLine(points):

Write a program that prompts the user to enter five points and displays whether
they are on the same line.'''

N = 5


def main():
    # Prompt the user to enter the three points for p0, p1, and p2
    points = (input("Please enter five points: "))  # 3.4 2 6.5 9.5 2.3 2.3 5.5 5 -5 4

    lst = createList(points)

    displayResult(lst)


# Create a list
def createList(points):
    # Convert input to float
    lst = [float(x) for x in points.split(" ")]

    # Create empty lists
    x = []
    y = []

    # Extract x and y coordinates from list
    for i in range(0, len(lst), +2):
        x.append(lst[i])
        y.append(lst[i + 1])

    mergedList = [list(a) for a in zip(x, y)]

    return mergedList


# Display result
def displayResult(lst):
    if sameLine(lst):
        str = "on"
    else:
        str = "not on"

    print(f"The 5 points are {str} the same line")


# Return true if point (x2, y2) is on the same line from (x0, y0) to (x1, y1)
def sameLine(lst): # TO-DO
    for i in range(N):
        for j in range(N):
            if isOnTheSameLine(lst[i][0], lst[i][1],
                               lst[i + 1][0], lst[i + 1][1],
                               lst[i + 2][0], lst[i + 2][1],
                               lst[i + 3][0], lst[i + 3][1],
                               lst[i + 4][0], lst[i + 4][1]):
                return False

        return True


# Return true if point (x2, y2) is on the same line from (x0, y0) to (x1, y1)
def isOnTheSameLine(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) \
           * (x3 - x0) * (y3 - y0) * (x4 - x0) * (y4 - y0) == 0


main()  # Invoke main function
