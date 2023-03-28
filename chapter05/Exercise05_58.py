# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Reverse a string) Write a program that prompts the user to enter a string and
displays the string in reverse order.'''

# Prompt the user to enter a string
s1 = input("Please enter a string: ")

# Assign values
s2 = ""
s3 = ""

# Reverse the string f1
for i in range(0,len(s1)):
    s2 = s1[i] + s2

# Reverse the string f2
for i in range(len(s1) -1, -1, -1):
    s3 += s1[i]

# Display result
print(s2)
print(s3)




