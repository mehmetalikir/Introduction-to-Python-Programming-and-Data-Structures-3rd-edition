# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Palindromic prime) A palindromic prime is a prime number and also palindromic.
For example, 131 is a prime and also a palindromic prime, as are 313 and
757. Write a program that displays the first 100 palindromic prime numbers. Display
10 numbers per line, separated by exactly one space, as follows:
2 3 5 7 11 101 131 151 181 191
313 353 373 383 727 757 787 797 919 929'''

# Return the reversal of an integer, i.e. reverse(456) returns 654
def reverse(number):
    number = str(number)
    reversed = ""

    for i in range(0, len(number), +1):
        reversed = number[i] + reversed

    return reversed


# Return true if number is a palindrome
def isPalindrome(number):

    if number == int(reverse(number)):  # Check whether number is palindrome
        return True
    else:
        return False

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not a prime
            return False
        divisor += 1

    return True  # Number is prime
def printPalindromicPrimeNumbers():
    number = 2  # A number to be tested for palindromic primeness
    count = 0 # Count the number of palindromic prime numbers

    # Repeatedly find palindromic prime numbers
    while count <= 100:
        if isPrime(number) and isPalindrome(number): # Check whether number is palindromic prime
            print(f"%-10s" % number, end = "")
            count += 1
            if count % 10 == 0:
                print() # Jump to the new line
        number += 1
def main():

    printPalindromicPrimeNumbers()

main()


