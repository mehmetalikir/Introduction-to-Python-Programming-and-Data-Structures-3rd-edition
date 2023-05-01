# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: find the highest point) In computational geometry, often you need to
find the topmost point in a set of points. Write the following function that
returns the topmost point in a set of points:

    # Return a list of two values for a point
    def getTopmostPoint(points):

Write a test program that prompts the user to enter the coordinates of six points
and displays the topmost point'''


def main():
    line = input("Enter six points: ").split()  # 5 6 -5 7 0 7 5 12 4 8 3 11
    xy = [[float(line[i]), float(line[i + 1])] for i in range(0, 12, 2)]

    point = getToptmostPoint(xy)

    print(f"The topmost point is {point[0], point[1]}")

    # print("The topmost point is (" +
    #
    #       str(point[0]) + ", " + str(point[1]) + ")")


def getToptmostPoint(xy):
    topmostindex = 0
    topmost = xy[0][1]
    x = 0
    y = 0

    for i in range(1, len(xy)):
        if topmost < xy[i][1]:
            topmost = xy[i][1]
            topmostindex = i

        x = xy[topmostindex][0]
        y = xy[topmostindex][1]

    return [x, y]


main()  # Invoke main function
