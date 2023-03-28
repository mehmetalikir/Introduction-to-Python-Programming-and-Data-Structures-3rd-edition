# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Occurrence of max numbers) Write a program that reads integers, finds the largest
of them, and counts its occurrences. Assume that the input ends with number
0. Suppose that you entered 3 5 2 5 5 5 0; the program finds that the largest
is 5 and the occurrence count for 5 is 4.
(Hint: Maintain two variables, max and count. max stores the current max number,
and count stores its occurrences. Initially, assign the first number to max
and 1 to count. Compare each subsequent number with max. If the number is
greater than max, assign it to max and reset count to 1. If the number is equal to
max, increment count by 1.)'''

# Assign the first number to max
max = int(input("Please enter an integer: "))

# Assign values
count = 0
number = 1

# Compare each subsequent number with max
while number > 0:
    number = int(input("Please enter an integer: "))
    if number > max:
        max = number
        count = 0
    if number == max:
        count += 1

# Display result
print("The largest number is", max)
print("The occurrence count of the largest number is ", count)

