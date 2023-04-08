# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


''' (Financial: credit card number validation) Credit card numbers follow certain patterns.
 A credit card number must have between 13 and 16 digits. It must start with:

  * 4 for Visa cards
  * 5 for Master cards
  * 37 for American Express cards
  *
  6 for Discover cards

 In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card
 numbers. The algorithm is useful to determine whether a card number is entered
 correctly or whether a credit card is scanned correctly by a scanner. Credit card
 numbers are generated following this validity check, commonly known as the
 Luhn check or the Mod 10 check, which can be described as follows (for illustration,
 consider the card number 4388576018402626):

 1. Double every second digit from right to left. If doubling of a digit results in a
    two-digit number, add up the two digits to get a single-digit number.

 2. Now add all single-digit numbers from Step 1.
                 4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37

 3. Add all digits in the odd places from right to left in the card number.
                 6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38

 4. Sum the results from Step 2 and Step 3.
                 37 + 38 = 75

 5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise,
    it is invalid. For example, the number 4388576018402626 is invalid, but the
    number 4388576018410707 is valid.

 Write a program that prompts the user to enter a credit card number as an
 integer. Display whether the number is valid or invalid. Design your program to
 use the following methods:

'''


# Return true if the card number is valid
def isValid(number):
    if 13 <= getSize(number) <= 16 and \
            (prefixMatched(number, 4) or prefixMatched(number, 5) or
             prefixMatched(number, 6) or prefixMatched(number, 37)) and \
            ((sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0):
        return True
    else:
        return False


# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    sum = -1
    while number > 0:
        number //= 10  # Jump to second digit
        sum += getDigit((number % 10) * 2)
    return sum


# Return this number if it is a single digit, otherwise,
# return the sum of the two digits
def getDigit(number):
    if number <= 9:
        return number
    else:
        return number // 10 + number % 10


# Return sum of odd place digits in number
def sumOfOddPlace(number):
    sum = -1
    while number > 0:
        sum += number % 10
        number //= 100  # Jump to odd place
    return sum


# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    if getPrefix(number, getSize(d)) == d:
        return True
    else:
        return False


# Return the number of digits in d
def getSize(d):
    count = 0
    while d > 0:
        d //= 10
        count += 1
    return count


# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number.
def getPrefix(number, k):
    for i in range(0, getSize(number) - k, +1):
        number //= 10
    return number


def main():
    # Prompt the user to enter a credit card number as an integer
    number = int(input("Please enter a credit card number as an integer: "))
    if isValid(number):
        print(f"{number} is valid")
    else:
        print(f"{number} is invalid")


main()
