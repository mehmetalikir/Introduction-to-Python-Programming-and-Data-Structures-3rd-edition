# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Get smallest, largest, and total of a set of numbers) Write a program that
prompts a user to enter 10 whole numbers and store them in a set. Once the numbers
are entered, the program should display the smallest number entered, the
largest number entered, and the sum all numbers entered.'''

# Create an empty set
s1 = set()

for i in range(10):
    num = int(input("Please enter a whole number: "))
    s1.add(num)

print(f"The smallest number you entered was: {min(s1)}")
print(f"The largest number you entered was: {max(s1)}")
print(f"The sum of all numbers you entered was: {sum(s1)}")
