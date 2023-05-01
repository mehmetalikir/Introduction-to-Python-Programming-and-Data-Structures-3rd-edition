# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Algebra: solve linear equations) Write a function that solves the following
2 x 2 system of linear equations:

The function header is:

    def linearEquation(a, b):

The function returns None if a00a11 - a01a10 is 0. Write a test program that
prompts the user to enter a00, a01, a10, a11, b0, and b1, and displays the result.
If a00a11 - a01a10 is 0, report that “The equation has no solution'''


def main():
    # Prompt the user to enter a00, a01, a10, a11, b0, and b1
    a = float(input("Please enter a00: "))
    b = float(input("Please enter a01: "))
    c = float(input("Please enter a10: "))
    d = float(input("Please enter a11: "))
    e = float(input("Please enter b0: "))
    f = float(input("Please enter b1: "))
    A = [[a, b], [c, d]]
    B = [e, f]

    result = linearEquation(A, B)

    # Display the result
    if result == None:
        print("The equation has no solution")
    else:
        print("x is", result[0], "and y is", result[1])

# Solve linear equation
def linearEquation(a, b):
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]

    if determinant == 0:
        return None
    else:
        result = []
        x = (b[0] * a[1][1] - b[1] * a[0][1]) / determinant
        y = (b[1] * a[0][0] - b[0] * a[1][0]) / determinant
        result.append(x)
        result.append(y)
        return result


main()  # Invoke main function
