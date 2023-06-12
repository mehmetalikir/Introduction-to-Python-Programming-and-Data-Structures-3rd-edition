# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Triangular number iterator) A triangular number is defined as n(n + 1)/2 for
n = 1, 2, ..., and so on.So, the first few numbers are 1, 3, 6, 10, 15, etc. Write an
iterator class for triangular numbers, Invoking the __next__() method should
return the next triangular number. Write a test program that displays all triangular
numbers less than 1000, ten per line

1 3 6 10 15 21 28 36 45 55
66 78 91 105 120 136 153 171 190 210
231 253 276 300 325 351 378 406 435 465
496 528 561 595 630 666 703 741 780 820
861 903 946 990'''


class TriangularNumberIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
        self.triangular = 0
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:  # Check if the limit is reached
            raise StopIteration

        self.current += 1
        self.triangular += self.current  # Calculate the triangular number
        self.count += 1

        return self.triangular  # Return the triangular number


# Display all triangular numbers less than 1000, ten per line
def displayTriangularNumbers(limit):
    iterator = TriangularNumberIterator(limit)
    numbers = []

    for num in iterator:
        numbers.append(str(num))  # Add the triangular number to the list
        if len(numbers) == 10:
            print(" ".join(numbers))  # Display the numbers on one line
            numbers = []  # Reset the list of numbers

    if numbers:
        print(" ".join(numbers))  # Display any remaining numbers


displayTriangularNumbers(1000)  # Call the function
