# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Twin primes) Twin primes are a pair of prime numbers that differ by 2. For example,
3 and 5, 5 and 7, 11 and 13 are twin primes.
Write a program to find all twin primes less than 1,000. Display the output as follows:
(3, 5)
(5, 7)
....'''

# Return the reversal of an integer, i.e. reverse(456) returns 654
def reverse(number):
    number = str(number)
    reversed = ""

    for i in range(0, len(number), +1):
        reversed = number[i] + reversed

    return reversed


def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not a prime
            return False
        divisor += 1

    return True  # Number is prime


def printTwinPrimes():
    number = 2  # A number to be tested for twin primeness

    # Repeatedly find twin prime numbers
    while number <= 1_000:
        if isPrime(number) and isPrime(number + 2):  # Check whether number is twin prime
            print("(", number, ",", (number + 2), ")")

        number += 1


def main():
    printTwinPrimes()


main()
