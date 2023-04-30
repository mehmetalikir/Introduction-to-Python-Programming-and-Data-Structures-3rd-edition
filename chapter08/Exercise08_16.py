# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Sort a list of points on y-coordinates) Write the following function to sort a list
of points on their y-coordinates. Each point is a list of two values for x- and y coordinates.

    # Returns a new list of points sorted on the y-coordinates
    def sort(points):

For example, the points [[4, 2], [1, 7], [4, 5], [1, 2], [1, 1], [4, 1]] will be sorted
to [[1, 1], [4, 1], [1, 2], [4, 2], [4, 5], [1, 7]]. Write a test program that displays
the sorted result for points [[4, 34], [1, 7.5], [4, 8.5], [1, -4.5], [1, 4.5],
[4, 6.6]] using print(list).'''


def main():
    # Assign values
    points = [[4, 34], [1, 7.5], [4, 8.5], [1, -4.5], [1, 4.5], [4, 6.6]]
    print(sort(points))


# Returns a new list of points sorted on the y-coordinates
def sort(points):
    # Swap x- and y-coordinates in each point
    temp = [[y, x] for [x, y] in points]
    temp.sort(reverse=True)

    return [[x, y] for [y, x] in temp]


main()  # Invoke main function
