# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Binary to decimal) Write a recursive function that parses a binary number as a
string into a decimal integer. The function header is as follows:

    def binaryToDecimal(binaryString):

Write a test program that prompts the user to enter a binary string and displays its
decimal equivalent.'''


def main():
    binaryString = input("Please enter a binary string: ")
    decimal = binaryToDecimal(binaryString)
    print("Decimal equivalent:", decimal)


def binaryToDecimal(binaryString):
    if len(binaryString) == 0:  # Base case: binary string is empty
        return 0
    else:
        lastDigit = int(binaryString[-1])  # Get the last digit of the binary string
        remainingDigits = binaryString[:-1]  # Get the remaining digits (excluding the last digit)

        # Recursively convert the remaining digits and multiply the result by 2,
        # then add the last digit to get the decimal equivalent
        return binaryToDecimal(remainingDigits) * 2 + lastDigit


main()
