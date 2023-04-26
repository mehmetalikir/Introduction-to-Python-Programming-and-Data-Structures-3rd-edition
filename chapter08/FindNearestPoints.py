import NearestPoints


def main():
    numberOfPoints = int(input("Enter the number of points: "))

    # Create a list to store points
    points = []
    for i in range(numberOfPoints):
        s = input("Enter x- and y-coordinates of point"
                  + str(i) + ": ")
        point = [float(x) for x in s.split()]
        points.append(point)

    # p1 and p2 are the indices in the points list
    p1, p2 = NearestPoints.nearestPoints(points)

    # Display result
    print("The closest two points are (" +
          str(points[p1][0]) + ", " + str(points[p1][1]) + ") and (" +
          str(points[p2][0]) + ", " + str(points[p2][1]) + ")")


main()  # Call the main function
