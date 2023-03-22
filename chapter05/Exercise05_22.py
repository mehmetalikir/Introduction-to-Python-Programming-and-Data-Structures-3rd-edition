# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display prime numbers between 1000 and 2000) Display all the prime numbers
between 1000 and 2000, inclusive and the total number of prime numbers.
Display 10 prime numbers per line.'''

# Constant
PER_LINE = 10

# Assign variable
count = 0
num = 1000

# Prints the prime numbers
while  1000 <= num <= 2000:
    isPrime = True
    divider = 2
    while divider <= num/2:
        if num % divider == 0:
            isPrime = False
            break
        divider += 1

    if isPrime:
        count += 1
        if count == PER_LINE:  # Display ten characters per line
            count = 0
            print(num, end=" ")
            print()
        else:
            print("", num, end=" ")
    num += 1

