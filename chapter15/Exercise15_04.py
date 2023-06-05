# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Calculate a number to a power) Write a function that calculates the result of
a number multiplied by itself a specified number of times. The program should
prompt the user for enter a number and the power, calculate the result using the
recursive function, and display the result.'''


# Calculate the result of a number multiplied by itself a specified number of times
def main():
    n = int(input("Please enter a number: "))
    p = int(input("Please enter the power: "))
    print(f"{n} to the power of {p} is {power(n, p)}")


def power(n, p):
    # Ensures that the recursive method is called until to p reaches 0
    if p == 0:
        return 1
    return n * power(n, p - 1)


main()
