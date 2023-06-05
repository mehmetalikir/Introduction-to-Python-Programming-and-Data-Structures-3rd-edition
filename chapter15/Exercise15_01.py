# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Sum the digits in an integer using recursion) Write a recursive function that computes
the sum of the digits in an integer. Use the following function header:

    def sumDigits(n):

For example, sumDigits(234) returns 2 + 3 + 4 = 9. Write a test program
that prompts the user to enter an integer and displays the sum of its digits.'''


def main():
    num = int(input("Please enter an integer: "))

    digitSum = sumDigits(abs(num))

    # Display result
    print(f"The sum of digits in {num} is", digitSum)


# Compute the sum of the digits in an integer
def sumDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigits(n // 10)


main()
