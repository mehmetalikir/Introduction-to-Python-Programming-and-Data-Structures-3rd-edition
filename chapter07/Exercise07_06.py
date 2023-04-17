# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Revise Listing 5.14, PrimeNumber.py) Listing 5.14 determines whether a number
n is prime by checking whether 2, 3, 4, 5, 6, . . . , n/2 is a divisor. If a divisor
is found, n is not prime. A more efficient approach is to check whether any of the
prime numbers less than or equal to 2n can divide n evenly. If not, n is prime.
Rewrite Listing 5.14 to display the first 50 prime numbers using this approach.
You need to use a list to store the prime numbers and later use them to check
whether they are possible divisors for n.'''
import math
NUMBER_OF_PRIMES = 50  # Number of primes to display


def main():
    # Create a list
    list1 = createList(NUMBER_OF_PRIMES)

    # Find prime numbers
    findPrimes(list1)


    # Display the list
    print("The first 50 prime numbers are:")
    displayList(list1)


def createList(NUMBER_OF_PRIMES):
    # Create a list
    list1 = NUMBER_OF_PRIMES * [0]

    # Return the list
    return list1

# Find prime numbers
def findPrimes(list1):
    count = 0  # Count the number of prime numbers
    n = 2  # A number to be tested for primeness

    # Repeatedly find prime numbers
    while count < NUMBER_OF_PRIMES:
        if isPrime(n):
            list1[count] = n
            count += 1  # Increase the count
        n += 1
    return n


# Display the list
def displayList(list1):
    # Display the list 10 on each line
    for i in range(len(list1)):
        if i % 10 == 0:  # Display the number and advance to the new line
            print(f"{list1[i]:5d}")
        else:
            print(f"{list1[i]:5d}", end='')


def isPrime(n):
    # Assume the number is prime
    isPrime = True  # Is the current number prime?

    # Test if number is prime
    divisor = 2
    while divisor <= math.sqrt(n):
        isPrime = True
        if n % divisor == 0:
            # If true, the number is not prime
            return False  # Set isPrime to false
        divisor += 1

    return isPrime


main()
