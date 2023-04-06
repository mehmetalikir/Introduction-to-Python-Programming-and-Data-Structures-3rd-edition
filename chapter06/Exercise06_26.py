# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Mersenne prime) A prime number is called a Mersenne prime if it can be written
in the form 2^p - 1 for some positive integer p. Write a program that finds all
Mersenne primes with p <= 31 and displays the output as follows:
p   2^p –1
----------
2   3
3   7
5   31'''

import math


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


def printMersennePrime():
    number = 2  # A number to be tested for mersenne primeness

    # Repeatedly find mersenne prime numbers
    print("p        2^p-1")
    print("--------------")
    while number <= 10:
        if isPrime(number):  # Check whether number is mersenne prime
            print(f"%-1d%10d" % (number, (math.pow(2, number) - 1)))

        number += 1


def main():
    printMersennePrime()


main()
