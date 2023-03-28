# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Math: combinations) Write a program that displays all possible combinations
for picking two numbers from integers 1 to 7. Also display the total number of
all combinations.'''

# Assign values
number1 = 1
number2 = 7
count = 0

# Pick two numbers from integers 1 to 7
for number1 in range(number1, number2+1):
    for number2 in range(number1+1, number2+1):
        print(number1, number2)
        count += 1

# Display result
print("Total number of all combinations: ", count)
