# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Sum series) Write a function to compute the following series:

    m(i) = 1 / 2 + 2 / 3 + ... + i / i + 1

Write a test program that displays the following table:
        i       m(i)
        1       0.5000
        2       1.1667
        ...
        19      16.4023
        20      17.3546 '''


def sumSeries():
    mi = 0
    print("i                m(i)") # Print header of table
    for i in range(1, 20, +1):
        mi += i / (i + 1) # Compute mi
        print(f"%-6d%17.4f" % (i, mi)) # Display result


def main():
    sumSeries() # Invoke function


main()
