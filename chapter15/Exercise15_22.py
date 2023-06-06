# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Hex to decimal) Write a recursive function that parses a hex number as a string
into a decimal integer. The function header is as follows:

    def hexToDecimal(hexString):

Write a test program that prompts the user to enter a hex string and displays its
decimal equivalent.'''


def main():
    # Prompt the user to enter a decimal number
    hexString = input("Please enter a hex number: ").strip()

    decimal = hexToDecimal(hexString)

    # Display result
    print("Decimal equivalent:", decimal)

# Parse a hex number as a string into a decimal integer
def hexToDecimal(hexString):
    return hexToDecimalHelper(hexString, 0, len(hexString) - 1)


def hexToDecimalHelper(hexString, low, high):
    if high < low: # Base case
        return 0
    else:
        if hexString[high] in 'ABCDEF':
            # If the digit is a hexadecimal letter, compute its decimal value
            temp = ord(hexString[high]) - ord('A') + 10
        else:
            # If the digit is a decimal digit, compute its decimal value
            temp = ord(hexString[high]) - ord('0')

        # Recursively call hexToDecimalHelper for the next lower digit
        return hexToDecimalHelper(hexString, low, high - 1) * 16 + temp


main()
