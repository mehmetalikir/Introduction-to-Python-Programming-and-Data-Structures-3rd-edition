# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Number of prime numbers) Programming Exercise 16.8 stores the prime numbers
in a file named file.dat. Write a program that finds the number
of prime numbers that are less than or equal to 10, 100, 1,000, 10,000,
100,000, 1,000,000, 10,000,000, 100,000,000, 1,000,000,000, and
10,000,000,000. Your program should read the data from file.dat.'''

def main():
    n = 10_000_000_000

    # Open the file and read the prime numbers
    with open("file.dat", "r") as file:
        primes = file.read().split()

    count = 0
    for prime in primes:
        if int(prime) <= n:
            count += 1
        else:
            break

    print("The total number of prime numbers <= ", n, " is ", count)


main()
